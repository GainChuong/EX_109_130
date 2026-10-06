def dep_calc(p, t, s, y):
    global result
    org_p=p+t+s
    year_dep=org_p/y
    month_dep=year_dep/12
    final_dep=org_p
    result_list=[]
    for i in range(y):
        final_dep-=year_dep
        result=f"Năm{i+1}, Sau khấu hao còn => {final_dep}"
        result_list.append(result)
    return org_p, year_dep, month_dep, result_list
if __name__ == "__main__":
    new_price=float(input("Giá mua mới: "))
    transportation_cost=float(input("Phí vận chuyển là: "))
    setup_cost=float(input("Phí lắp đặt: "))
    year_usage=int(input("Số năm sử dụng dự kiến là: "))
    origin_price, year_dep,month_dep, result_list=dep_calc(new_price,transportation_cost,setup_cost, year_usage)
    print(f"Nguyên giá TSCĐ là: {origin_price}\n"
          f"Mức trích khấu hao năm là: {year_dep}\n"
          f"Mức trích khấu hao tháng là {month_dep}\n")
    for i in result_list:
        print(i)