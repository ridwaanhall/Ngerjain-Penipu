'''
formservices%5B%5D=70e6e51d4c7226c924940efda278651a&Phone=1232+1321+3123+1232&tildaspec-mask-Phone=9999+9999+9999+9999&Phone_2=12+32&tildaspec-mask-Phone_2=99+99&Phone_3=3213123&tildaspec-mask-Phone_3=9999999&Input=321321312321312312312321321312312&form-spec-comments=&tildaspec-cookie=&tildaspec-referer=http%3A%2F%2Fpilih.tarif.bni.tilda.ws%2Fdftr&tildaspec-formid=form652374741&tildaspec-formskey=1f87618a0dd09daeeded0b0117963768&tildaspec-version-lib=02.001&tildaspec-pageid=40317941&tildaspec-projectid=7963768&tildaspec-lang=EN&tildaspec-fp=6354646d6863346c656e2d55532c656e7057696e333276476f6f676c6520496e632e614d6f7a696c6c616e4e65747363617065706c696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d7669657765727072317737363368363436&tildaspec-tildacaptcha=03AFcWeA7xxeDEF0rqcqUht7MnIfWWXa3kf9VyEACfNQYQxi-ZNrSacHoCk46e24Ktj89J2qfY1Tz6c59TWnSXJySW0h_xJYbhudDgxe6NrrA-OS5Yj3tzzn30RnbSuNMCAf2TOTIC3xfQl2D_Nlm2Lm4W294gbdnbWK6tOmircIK7nOWycXhdkG3VC90KrMogX1i5ZfOIRWW1Zg_1PlkaKRPBa6F8aBbPDc4cSFKcf_wgAC-ZpwreWA7JSF3-DJ9ba0ufLcE16JK8lm_r6mmcjSpHWlq88C1sdY4WbzgJo3bmzf9Zap2VmaHZUJcAwbAjB_MzXchYJKKucfUdYgeGtoLw4TgcPH7T21v9msyH_q1ZuVCyMyumaKL2DaUPmJs1PZwCefy1xbAtYyjkJri4KxOQveNhNxhWqLZWTjMAVh3Wkx66s0IwbKqRl4A7l-7QmTO-YiXkEfaFJLYsfGq4n1ctuScj2q9lSDcnUeuikyxuSEUspXruSaVrRpDegGZVnzIBARad-iY_xsemf3gzpo2dqxk63TPkmtOQBt9T01KJFIP8ZRx-irU
'''


import requests
import random

url = 'https://forms.tildacdn.com/procces/'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
loop_value = int(input("bar bar brp kali? : "))

for i in range(1, loop_value+1):
    start_nodeb = 4219313719837212
    end_nodeb = 9999999999999999
    random_number_deb = random.randint(start_nodeb, end_nodeb)
    random_nodeb = '{:04} {:04} {:04} {:04}'.format(
        random_number_deb // 10**12 % 10**4,
        random_number_deb // 10**8 % 10**4,
        random_number_deb // 10**4 % 10**4,
        random_number_deb % 10**4
    )
    aa = str(random.randint(1, 12)).zfill(2)
    bb = str(random.randint(23, 99))
    random_mb = f"{aa}/{bb}"
    
    random_number_cvv = random.randint(1, 9999999)
    random_cvv = '{:07}'.format(random_number_cvv)
    
    data = {
        'formservices[]': '70e6e51d4c7226c924940efda278651a',
        'Phone': '1232 1312 3123 2132',
        'tildaspec-mask-Phone': '9999 9999 9999 9999',
        'Phone_2': '12 32',
        'tildaspec-mask-Phone_2': '99 99',
        'Phone_3': '1232132',
        'tildaspec-mask-Phone_3': '9999999',
        'Input': '123213213213123123123131',
        'form-spec-comments': '',
        'tildaspec-cookie': '',
        'tildaspec-referer': 'http://pilih.tarif.bni.tilda.ws/dftr',
        'tildaspec-formid': 'form652374741',
        'tildaspec-formskey': '1f87618a0dd09daeeded0b0117963768',
        'tildaspec-version-lib': '02.001',
        'tildaspec-pageid': '40317941',
        'tildaspec-projectid': '7963768',
        'tildaspec-lang': 'EN',
        'tildaspec-fp': '6354646d6863346c656e2d55532c656e7057696e333276476f6f676c6520496e632e614d6o'
    }

    response = requests.post(url, data=data, headers=headers)

    # Mengecek apakah permintaan berhasil
    if response.status_code == 200:
        print("Permintaan POST berhasil")

        # Menampilkan isi respons
        print("Isi Respons:")
        print(response.text)  # Jika kamu ingin teks respons
        # atau
        # print(response.content)  # Jika kamu ingin konten biner respons

    else:
        print(f"Permintaan POST gagal. Kode status: {response.status_code}")

