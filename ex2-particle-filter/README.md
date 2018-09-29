Số particle: tùy ý, ví dụ: 100

Tần số tín hiệu điều khiển robot: 40 Hz (t = 0.025s)

Tần số hoạt động của laser rangefinder: 5 Hz (cứ sau 8 tín hiệu điều khiển thì laser sensor đọc dữ
liệu 1 lần)

_xtruek_ = [ _xk yk φk_ ]
_T_
: true robot pose at time step _k_

XTRUE = [ _xtrue_ 1 _xtrue_ 2 _... xtrueN_ ] , ma trận kích thước 3xN, N = 625: # time step

XODO: ma trận kích thước 3xN, robot pose ước lượng từ process model (tính toán với vận tốc V
và steering angle G bị nhiễu)

_lm_ =
[

```
x 1
y 1
```
```
x 2
y 2
```
## ...

## ...

```
x 10
y 10 ], (x l ,y l ): tọa độ của landmark thứ l
```
Z: ma trận 3x5xN: measurements, ví dụ:

Z(:,:,32) = [17.2502 11.9829 26.4415 NaN NaN
1.2185 0.4538 0.9034 NaN NaN
2.0000 3.0000 4.0000 NaN NaN]
nghĩa là tại time step _k_ = 32, robot phát hiện 3 landmark gồm landmark thứ 2, 3 và 4 (xem hàng
thứ 3), khoảng cách range từ robot đến các landmark này lần lượt là 17.2502, 11.9829 và
26.4415 m (hàng thứ 1), góc bearing đến các landmark này lần lượt là 1.2185, 0.4538 và 0.
radian (hàng thứ 2).

Nhiễu laser rangefinder: _σrange_ =0.2 _m,σbearing_ =^2
_o_

VG: ma trận 2xN: hàng thứ nhất V là vận tốc (m/s), hàng thứ hai G là góc lái steering angle
(radian); đây là các giá trị đo được bằng cảm biến nên đã chịu ảnh hưởng của noise (
_σV_ =0.5 _m_ / _s,σsteering_ = 3 _o_ ) (các particle được tạo ra bằng cách tiếp tục thêm noise vào các giá trị V
và G nêu trên, vận tốc thật Vtrue = 5 m/s và góc lái thật Gtrue không cần biết).

Dữ liệu trong file data20171107.m: XTRUE, XODO, Z, lm, VG

Lưu ý: chuyển đổi đơn vị đo góc phù hợp.
----------------------------------

1. Vẽ quỹ đạo (x,y) của robot: xtrue, xodo và của 3 particle có trọng số lớn nhất, trung bình
    và nhỏ nhất, sử dụng Particle Filter.
2. Tính sai số RMS (root mean square) giữa các quỹ đạo so với quỹ đạo thực.
3. Lặp lại 2 câu trên sử dụng Extended Kalman Filter.

Các nhóm nộp code + báo cáo vào ngày 7/11.