import requests
import os
import schedule

D = {'Электротехника': [3950,
                        3951,
                        3952,
                        3953,
                        3954,
                        3955,
                        3956,
                        198,
                        3723,
                        3724,
                        3725,
                        3726,
                        3727,
                        3728,
                        3730,
                        3731,
                        3732,
                        3733,
                        3734,
                        3735,
                        3736,
                        3738,
                        3739,
                        3740,
                        3741,
                        3742,
                        3743,
                        3744,
                        3745,
                        3746,
                        3748,
                        3749,
                        3750,
                        3751,
                        3752,
                        3753,
                        4623,
                        4624,
                        3755,
                        3756,
                        3757,
                        3758,
                        4562,
                        3759,
                        3761,
                        3762,
                        3763,
                        3764,
                        3765,
                        3766,
                        3767,
                        3768,
                        3769,
                        3770,
                        3771,
                        3772,
                        3773,
                        3775,
                        3776,
                        3778,
                        3779,
                        3780,
                        3781,
                        3782,
                        3783,
                        3784,
                        3785,
                        3786,
                        3787,
                        3789,
                        3790,
                        3791,
                        3792,
                        3793,
                        3794,
                        3795,
                        4641,
                        4642,
                        3797,
                        3798,
                        3799,
                        3800,
                        3801,
                        4581,
                        3802,
                        3804,
                        3805,
                        3806,
                        3807,
                        3808,
                        3809,
                        3811,
                        3812,
                        3813,
                        3814,
                        3815,
                        3816,
                        3817,
                        3818,
                        3820,
                        3821,
                        3822,
                        3823,
                        3824,
                        3825,
                        3826,
                        3827,
                        3828,
                        3829,
                        3830,
                        4565,
                        4566,
                        3831,
                        4584,
                        4585,
                        4586,
                        4587,
                        3833,
                        3834,
                        3835,
                        3836,
                        3837,
                        3838,
                        3839,
                        4639,
                        3842,
                        3843,
                        3844,
                        3845,
                        3846,
                        3847,
                        3848,
                        3849,
                        3850,
                        3851,
                        3852,
                        3853,
                        3854,
                        3856,
                        3857,
                        3858,
                        3859,
                        3860,
                        3861,
                        3862,
                        3863,
                        3864,
                        3865,
                        3867,
                        3868,
                        3869,
                        3870,
                        3871,
                        3872,
                        3873,
                        3874,
                        3875,
                        3877,
                        3878,
                        3879,
                        3880,
                        3881,
                        3882,
                        3883,
                        3884,
                        3885,
                        3886,
                        3887,
                        3888,
                        3889,
                        3890,
                        3891,
                        3892,
                        3893,
                        3894,
                        3895,
                        3897,
                        3899,
                        3900,
                        3901,
                        3902,
                        3903,
                        3904,
                        3905,
                        3906,
                        3907,
                        3908,
                        4583,
                        3910,
                        3911,
                        3912,
                        3913,
                        3914,
                        3915,
                        3916,
                        3917,
                        3918,
                        3919,
                        3921,
                        3923,
                        3924,
                        3925,
                        3926,
                        3928,
                        3929,
                        3930,
                        3931,
                        3932,
                        3933,
                        3934,
                        3935,
                        3936,
                        3937,
                        3938,
                        3939,
                        3940,
                        3942,
                        3943,
                        3944,
                        3945,
                        3946,
                        3947,
                        3948,
                        3949,
                        3957,
                        3958]}


def job():
    print('Start...')
    list_id = set()
    for elem in D['Электротехника']:
        a = requests.get(
            'http://m1.1-2.su/api/products?sections[]=' + str(elem),
            auth=(160399, 'cjp4amd')).json()
        last = a['meta']['last_page']
        print(elem, len(list_id))

        for i in range(1, int(last) + 1):
            b = requests.get(
                f'http://m1.1-2.su/api/products?page={str(i)}&sections[]=' + str(
                    elem), auth=(160399, 'cjp4amd')).json()
            for elem_2 in b['data']:
                list_id.add(elem_2['id'])
    list_id = list(list_id)
    from bs4 import BeautifulSoup
    session = requests.Session()
    per_session = session.post("http://www.1-2.su/site/login",
                               data={'LoginForm[login]': '160399',
                                     'LoginForm[password]': 'cjp4amd'})

    def pars(id):
        bsObj = BeautifulSoup(
            session.get(f"http://www.1-2.su/catalog/product/id/{id}").content,
            'html.parser')
        name = bsObj.find("h1").text
        count = "".join(
            bsObj.find_all("table", class_="table")[-1].find(
                "tbody").text.split(
                "Количество:")[-1]).split()
        data = bsObj.find_all("table", class_="table")[-2].find(
            "tbody").text.split()
        price = bsObj.find_all("table", class_="table")[0].find("tbody").find(
            'td').text
        text_data = ""
        description = ""
        weight = ''
        if "Характеристики" in [j.text for j in bsObj.find_all("h2")]:
            key = bsObj.find("dl").find_all("dt")
            value = bsObj.find("dl").find_all("dd")
            for i in range(len(bsObj.find("dl").find_all("dt"))):
                if 'Вес' in key[i].text:
                    weight = value[i].text
                text_data += key[i].text + ": " + 'S[' + str(
                    value[i].text) + ']' + "; "
        if "Описание" in [j.text for j in bsObj.find_all("h2")]:
            description = bsObj.find_all("p")[-1].text
        path = "///".join(
            bsObj.find('ol', class_="breadcrumb").text.strip().split("\n"))
        img = bsObj.find_all("img")
        img_data = ''
        if len(img) >= 2:
            img_data = img[-1]['src']
        return (
            name, description, count, data, text_data, path, img_data, price,
            weight)

    import pandas as pd
    import time

    df = pd.DataFrame(
        {'Product code': [], 'Product id': [], 'Category': [], 'Features': [],
         'Detailed image URL': [], 'Description': [], 'Weight': [],
         'Price': [],
         'Quantity': [], 'Product name': []})
    i = 0
    start_time = time.time()
    for elem in list_id[75:175]:
        try:
            i += 1
            name, description, amount, data, text_data, path, img_data, price, weight = pars(
                str(elem))
            amount = sum(map(int, amount[:3]))
            print(i, elem)
            weight = str(weight).strip()
            if amount > 0:
                if weight:
                    df = df.append(
                        {'Product code': data[-2], 'Product id': data[0],
                         'Category': path,
                         'Features': text_data, 'Detailed image URL': img_data,
                         'Description': description,
                         'Weight': float(weight) / 1000,
                         'Price': float(price.strip()),
                         'Quantity': amount, 'Product name': name},
                        ignore_index=True)
                else:
                    df = df.append(
                        {'Product code': data[-2], 'Product id': data[0],
                         'Category': path,
                         'Features': text_data, 'Detailed image URL': img_data,
                         'Description': description,
                         'Weight': weight,
                         'Price': float(price.strip()),
                         'Quantity': amount, 'Product name': name},
                        ignore_index=True)
        except Exception as e:
            print(e)
            continue
    print(time.time() - start_time)
    try:
        df_last = pd.read_csv('Electrotexnica.csv')
        df_res = df_last[~df_last['Product id'].isin(df['Product id'])]
    except:
        pass
    try:
        os.remove('Electrotexnica.csv')
    except:
        pass
    try:
        os.remove('data_last.csv')
    except:
        pass
    df.to_csv('Electrotexnica.csv')
    try:
        df_res.to_csv('data_last.csv')
    except:
        pass


schedule.every(48).hours.do(job)
job()
while True:
    schedule.run_pending()
