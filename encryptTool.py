# 这是系统的登录界面
import tkinter
from tkinter import messagebox
from Crypto.Cipher import AES
import base64
import time
import binascii
from binascii import a2b_hex
import json
import hashlib
from tkinter import ttk # 导入ttk模块，因为下拉菜单控件在ttk中


class Encrypt(object):
     def __init__(self):
          # 创建主窗口,用于容纳其它组件
          self.root = tkinter.Tk()
          # 给主窗口设置标题内容
          self.root.title("AES 和 MD5 加密工具")
          self.root.geometry('450x700')
    # 运行代码时记得添加一个gif图片文件，不然是会出错的
          self.canvas = tkinter.Canvas(self.root, height=200, width=500)#创建画布
          # self.image_file = tkinter.PhotoImage(file='welcome_1.gif')#加载图片文件
          # self.image = self.canvas.create_image(0,0, anchor='nw', image=self.image_file)#将图片置于画布上
          self.canvas.pack(side='top')# 放置画布（为上端）


          # 创建一个`label`名为`Phone: `
          self.label_Phone = tkinter.Label(self.root, text='手机号: ')
          self.label_AES_Key = tkinter.Label(self.root, text='AES_key: ')
          # 创建一个`label`名为`AESResult: `
          self.label_AESResult = tkinter.Label(self.root, text='手机号AES加密结果: ')
          # 创建一个`label`名为`Content: `
          # wraplength： 指定多少单位后开始换行
          # justify:  指定多行的对齐方式
          # ahchor： 指定文本(text)或图像(bitmap/image)在 Label 中的显示位置
          # 可用的值：
          # e/w/n/s/ne/se/sw/sn/center
          self.label_Content = tkinter.Label(self.root, text='Content:\n示例一：\n{"gender": 2,\n"phone":"18920190101",\n"name":"坐车"}\n\n"示例二：写加密后phone" ',wraplength = 90,justify='left')
          # 创建一个`label`名为`Key: `
          self.label_Key = tkinter.Label(self.root, text='Key: ')
          # 创建一个`label`名为`Md5Result: `
          self.label_Md5Result = tkinter.Label(self.root, text='ContentMd5加密\n结果sign值: ',justify='left')


          # 创建一个手机号输入框,并设置尺寸
          self.input_Phone = tkinter.Entry(self.root, width=30)
          # 创建一个AES Key输入框,并设置尺寸
          # defaultAESKey = "aaaaaaabbbbcccc1"
          # self.input_AES_Key = tkinter.Entry(self.root, width=30)
          # self.input_AES_Key.insert(0, defaultAESKey)

          # number = tkinter.StringVar()
          # self.combobox_AES_Key = ttk.Combobox(self.root, width=27, textvariable=number)
          self.combobox_AES_Key = ttk.Combobox(self.root, width=27)
          self.combobox_AES_Key['values'] = ("aaaaaaabbbbcccc1", "yuDA4rnmzNlm9zYo")  # 设置下拉列表的值
          # self.combobox_AES_Key.grid(column=1, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
          self.combobox_AES_Key.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

          # 创建一个AES加密结果文本区域显示框,并设置尺寸
          # self.input_AESResult = tkinter.Text(self.root, show='*',  width=30)
          self.input_AESResult = tkinter.Text(self.root, height=9,width=30)
          # 创建一个Content输入框,并设置尺寸
          # self.input_Content = tkinter.Entry(self.root, width=30)
          self.input_Content = tkinter.Text(self.root,height=17,width=30)
          # 创建一个Md5 Key输入框,并设置尺寸
          defaultKey = "xgwzrf4pv25tu7y6begl"
          self.input_Key = tkinter.Entry(self.root, width=30)
          self.input_Key.insert(0, defaultKey)
          # self.input_Key = tkinter.Entry(self.root, textvariable=defaultKey, width=30)
          # 创建一个MD5加密结果文本区域显示框,并设置尺寸
          self.input_Md5Result = tkinter.Text(self.root, height=10,width=30)


          # 创建一个AES加密按钮
          self.AESEncrypt_button = tkinter.Button(self.root, command = self.AESEncrypt_button_event, text = "AES加密", width=10)
          # 创建一个MD5的按钮
          self.Md5Encrypt_button = tkinter.Button(self.root, command = self.Md5Encrypt_button_event, text = "Md5加密", width=10)

         # AES参数的初始化
          # key值（密码）

          # self.key = 'aaaaaaabbbbcccc1'.encode(
          #     "utf-8")  # 因为在python3中AES传入参数的参数类型存在问题，需要更换为 bytearray , 所以使用encode编码格式将其转为字节格式（linux系统可不用指定编码）
          # vi偏移量
          self.iv = '1365127901262396'.encode("utf-8")  # 编码
          self.mode = AES.MODE_CBC
          self.BS = AES.block_size
          self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
          self.unpad = lambda s: s[0:-ord(s[-1])]


     # 完成布局
     def gui_arrang(self):
          self.label_Phone.place(x=20, y= 70)
          self.label_AES_Key.place(x=20, y=95)
          self.label_AESResult.place(x=20, y= 115)

          self.input_Phone.place(x=135, y=70)
          # self.input_AES_Key.place(x=135, y=95)
          self.combobox_AES_Key.place(x=135, y=95)
          self.input_AESResult.place(x=135, y=120)

          self.AESEncrypt_button.place(x=360, y=95)
          # self.siginUp_button.place(x=240, y=235)
          self.label_Content.place(x=20, y= 250)
          self.label_Key.place(x=20, y= 480)
          self.label_Md5Result.place(x=20, y= 510)
          self.input_Content.place(x=135, y=250)
          self.input_Key.place(x=135, y=480)
          self.input_Md5Result.place(x=135, y=510)
          self.Md5Encrypt_button.place(x=360, y=480)

     # AES加密方法
     def AESEncrypt(self, text):
         # 初始化AES参数中的 key
         # AESkey = self.input_AES_Key.get()
         AESkey = self.combobox_AES_Key.get()
         # print(AESkey)
         self.key = AESkey.encode(
               "utf-8")  # 因为在python3中AES传入参数的参数类型存在问题，需要更换为 bytearray , 所以使用encode编码格式将其转为字节格式（linux系统可不用指定编码）

         text = self.pad(text).encode("utf-8")
         # text = "15074891123"
         cryptor = AES.new(self.key, self.mode, self.iv)
         # 目前AES-128 足够目前使用(CBC加密)
         ciphertext = cryptor.encrypt(text)
         # 十六进制加密
         # print(binascii.b2a_hex(ciphertext).decode("utf-8"))
         return binascii.b2a_hex(ciphertext).decode("utf-8")
         # base64加密
         # return base64.b64encode(bytes(ciphertext))


     # 获取输入的手机号并进行AES加密
     def AESEncrypt_button_event(self):
          self.input_AESResult.delete(1.0,tkinter.END)
          # self.input_AESResult.delete(1.0, END)
          # Phone = self.input_Phone.get().ljust(10," ")
          Phone = self.input_Phone.get()
          e = self.AESEncrypt(Phone)  # 加密

          self.input_AESResult.insert(1.0, e)
          # Md5加密

     # Md5加密方法
     def Md5Encrypt(self, content):
          # 创建md5对象
          hl = hashlib.md5()

          # Tips
          # 此处必须声明encode
          # 否则报错为：hl.update(str)    Unicode-objects must be encoded before hashing
          hl.update(content.encode(encoding='utf-8'))
          return hl.hexdigest()
          # print('MD5加密前为 ：\n' + str)
          # print('MD5加密后为 ：' + hl.hexdigest())


     # 获取输入的content并进行Md5加密
     def Md5Encrypt_button_event(self):
          self.input_Md5Result.delete(1.0,tkinter.END)
          # self.input_Md5Result.delete(1.0, END)
          Content = self.input_Content.get("0.0", tkinter.END)
          # Content = self.input_Content.get().ljust(10, " ")
          # 将json转化为dict
          ContentDict = json.loads(s=Content)
          # print(ContentDict)
          # 手机号参数名为phone
          if(('phone' in ContentDict.keys())):
               if((len(ContentDict['phone']) == 11)):
                    encryptedPhone = self.AESEncrypt(ContentDict['phone'])
                    ContentDict['phone'] = encryptedPhone
          # 手机号参数名为sc_phone
          if(('sc_phone' in ContentDict.keys())):
               if((len(ContentDict['sc_phone'])==11)):
                    encryptedPhone = self.AESEncrypt(ContentDict['sc_phone'])
                    ContentDict['sc_phone'] = encryptedPhone



          # if(phone in ContentDict.keys()
          # print(ContentDict)

          #将dict转化为json,
          jsonResult = json.dumps(ContentDict,ensure_ascii=False)
          # key = "xgwzrf4pv25tu7y6begl"
          key = self.input_Key.get()
          # key = self.input_Key.get().ljust(10, " ")
          con= jsonResult+key
          noSpaceContent = con.replace(" ", "")
          print(noSpaceContent)

          e = self.Md5Encrypt(noSpaceContent)  # 加密
          print(e)
          self.input_Md5Result.insert(1.0, e)

          # self.root.destroy()
          # tkinter.messagebox.showinfo(title='影视资源管理系统', message='进入注册界面')





def main():
     # 初始化对象
     L = Encrypt()
     # 进行布局
     L.gui_arrang()
     # 主程序执行
     tkinter.mainloop()


if __name__ == '__main__':
     main()