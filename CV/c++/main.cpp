#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <opencv2/opencv.hpp>
typedef struct
{
	double left_x;
	double right_x;
	double up_y;
	double bottom_y;
	double aver_x;
	double aver_y;
	double aver_w;
	double aver_h;
} Area;

using namespace std;
using namespace cv;
void testShow(Mat img)
{
	namedWindow("img", WINDOW_NORMAL);
	imshow("img", img);
	waitKey(0);
}

Mat preTreat(Mat in_img)
{
	Mat gray_img, out_img;
	cvtColor(in_img, gray_img, CV_BGR2GRAY);				  //灰度
	threshold(gray_img, out_img, 225, 255, CV_THRESH_BINARY); //二值化
	return out_img;
}

vector<Rect> getBound(Mat img)
{
	vector<vector<Point>> contours; //轮廓
	vector<Vec4i> hierarchy;
	findContours(img, contours, hierarchy, RETR_TREE, CHAIN_APPROX_SIMPLE, Point(0, 0)); //寻找轮廓(参数可以再看下

	// 拟合矩形轮廓
	vector<Rect> boundRect;
	for (int i = 0, j = 0; i < contours.size(); i++)
	{
		Rect tmpRect;
		tmpRect = boundingRect(Mat(contours[i]));
		if (tmpRect.width < 80 || tmpRect.height < 35) //剔除太小的矩形
		{
			continue;
		}
		double ratio = (double)tmpRect.width / (double)tmpRect.height;
		if (ratio >= 2 && ratio <= 4) //保留宽高比约为3的矩形
		{
			boundRect.push_back(tmpRect);
		}
	}
	return boundRect;
	/*
	// 画矩形轮廓测试
	Mat drawing = Mat::zeros(img.size(), CV_8UC3);
	RNG rng(12345);
	for (int i = 0; i < boundRect.size(); i++)
	{
		Scalar color = Scalar(rng.uniform(0, 255), rng.uniform(0, 255), rng.uniform(0, 255));
		rectangle(drawing, boundRect[i].tl(), boundRect[i].br(), color, 2, 8, 0);
		cout << boundRect[i].x <<"|"<< boundRect[i].y <<"|" <<boundRect[i].width <<"|" <<boundRect[i].height << endl;
	}
	testShow(drawing);
	return boundRect;
	*/
}

vector<vector<Rect>> arrange(vector<Rect> boundRect)
{
	vector<vector<Rect>> detail; //保存确定的矩形
	vector<Rect> row;			 //保存每一行
	row.push_back(boundRect[boundRect.size() - 1]);
	for (int i = boundRect.size() - 2; i >= 0; i--)
	{
		Rect item = boundRect[i];
		if (abs(item.y - row[row.size() - 1].y) < 50)
		{
			row.push_back(item);
		}
		else
		{
			if (row.size() > 3)
			{
				detail.push_back(row);
			}
			row.clear();
			row.push_back(item);
		}
	}
	if (row.size() > 3)
	{
		detail.push_back(row);
	}
	/*
	for (int i = 0; i < detail.size(); i++)
	{
		for (int j = 0; j < detail[i].size(); j++)
		{
			cout << detail[i][j] << "|";
		}
		cout << endl;
	}
	*/
	return detail;
}

bool lessmark(const Rect &rect1, const Rect &rect2)
{
	return rect1.x < rect2.x;
}

bool greatermark(const Rect &rect1, const Rect &rect2)
{
	return rect1.x > rect2.x;
}

void getArea(vector<vector<Rect>> detail, Area &area)
{

	vector<int> left_x_list;
	vector<int> right_x_list;
	vector<int> up_y_list;
	vector<int> bottom_y_list;
	{
		for (int i = 0; i < detail[0].size(); i++)
		{
			up_y_list.push_back(detail[0][i].y);
		}
		sort(up_y_list.begin(), up_y_list.end());
		area.up_y = up_y_list[up_y_list.size() / 2];

		for (int i = 0; i < detail[detail.size() - 1].size(); i++)
		{
			bottom_y_list.push_back(detail[detail.size() - 1][i].y);
		}
		sort(bottom_y_list.begin(), bottom_y_list.end());
		area.bottom_y = bottom_y_list[bottom_y_list.size() / 2];

		for (int i = 0; i < detail.size(); i++)
		{
			sort(detail[i].begin(), detail[i].end(), lessmark);
			left_x_list.push_back(detail[i][0].x);
			right_x_list.push_back(detail[i][detail[i].size() - 1].x);
		}
		sort(left_x_list.begin(), left_x_list.end());
		sort(right_x_list.begin(), right_x_list.end());
		area.left_x = left_x_list[left_x_list.size() / 2];
		area.right_x = right_x_list[right_x_list.size() / 2];
	}
	area.aver_x = (area.right_x - area.left_x) / 6.0;
	area.aver_y = (area.bottom_y - area.up_y) / (double)(detail.size() - 1);
	area.aver_w = 0;
	area.aver_h = 0;
	int all_count = 0;
	for (int i = 0; i < detail.size(); i++)
	{
		for (int j = 0; j < detail[i].size(); j++)
		{
			area.aver_w += detail[i][j].width;
			area.aver_h += detail[i][j].height;
			all_count++;
		}
	}
	area.aver_w /= all_count;
	area.aver_h /= all_count;
}

void getOutDetail(double ***out_detail, vector<vector<Rect>> detail, Area area)
{
	double **col;
	double *item;
	for (int i = 0; i < detail.size(); i++)
	{
		col = new double *[7];
		for (int j = 0; j < 7; j++)
		{
			item = new double[2];
			col[j] = item;
			item[0] = area.left_x + area.aver_x * j + area.aver_w / 2;
			item[1] = area.up_y + area.aver_y * i;
		}
		out_detail[i] = col;
	}
}
int main()
{
	string src;
	cout << "请输入图片路径:";
	cin >> src;

	Mat img = imread(src);
	Mat preImg = preTreat(img);
	vector<Rect> boundRect = getBound(preImg);
	vector<vector<Rect>> detail = arrange(boundRect);
	Area area;
	getArea(detail, area);
	//cout << area.up_y << " " << area.bottom_y << " " << area.left_x << " " << area.right_x<<" "<<area.aver_h<<" "<<area.aver_w<<" "<<area.aver_x<<" "<<area.aver_y;
	double ***out_detail = new double **[detail.size()];
	getOutDetail(out_detail, detail, area);

	//以下为测试代码
	int radiusCircle = 20;
	Scalar colorCircle(0, 0, 255); // (B, G, R)
	for (int i = 0; i < detail.size(); i++)
	{
		for (int j = 0; j < 7; j++)
		{
			Point centerCircle1(out_detail[i][j][0], out_detail[i][j][1]);
			circle(img, centerCircle1, radiusCircle, colorCircle, FILLED);
		}
	}
	testShow(img);

	//清理内存
	for (int i = 0; i < detail.size(); i++)
	{
		for (int j = 0; j < 7; j++)
		{
			delete[] out_detail[i][j];
		}
		delete[] out_detail[i];
	}
	delete[] out_detail;
}