point_num = size(PP, 1);
acc_param = {'mean':[], 'var': [], rmse}
acc_mean = []; gyro_mean = []
part_norm = [];
part_rmse = [];
for i = 1:point_num
    start_point = PP(i, 1);
    end_point = PP(i, 2);
    part_acc = cal_acc(: , start_ppppoint: end_point);
    part_gyro = cal_gyro(: , start_point: end_point);
    part_mag = cal_mag(: , start_point: end_point);
    part_mean(1) = mean(part_acc);

end
