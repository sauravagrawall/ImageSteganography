# PIL module is used to extract
# pixels of image and modify it
from PIL import Image




# Convert encoding data into 8-bit binary
# form using ASCII value of characters
class encoded():
    password=""
    def genData(self,data):

            # list of binary codes
            # of given data
            newd = []

            for i in data:
                newd.append(format(ord(i), '08b'))
            return newd

    def putPassword(self,password):
        self.password=password;

    # Pixels are modified according to the
    # 8-bit binary data and finally returned
    def modPix(self,pix, data):

        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)

        for i in range(lendata):

            # Extracting 3 pixels at a time
            pix = [value for value in imdata.__next__()[:3] +
                                    imdata.__next__()[:3] +
                                    imdata.__next__()[:3]]

            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(0, 8):
                if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                    pix[j] -= 1

                elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                    if(pix[j] != 0):
                        pix[j] -= 1
                    else:
                        pix[j] += 1
                    # pix[j] -= 1

            # Eighth pixel of every set tells
            # whether to stop ot read further.
            # 0 means keep reading; 1 means thec
            # message is over.
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    if(pix[-1] != 0):
                        pix[-1] -= 1
                    else:
                        pix[-1] += 1

            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    def encode_enc(self,newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modPix(newimg.getdata(), data):

            # Putting modified pixels in the new image
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    # Encode data into image
    def data(self):
        data = input("Enter data to be encoded : ")
        return data
    def getPassword(self):
        return self.password
    def run(self):
        img = input("Enter image name(with extension) : ")

        image = Image.open(img, 'r')

        data = self.data()
        if (len(data) == 0):
            raise ValueError('Data is empty')

        newimg = image.copy()
        self.encode_enc(newimg, data)

        key= input("Enter password to secure the message: ")
        self.putPassword(key)

        new_img_name = input("Enter the name of new image(with extension) : ")
        newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

    # Decode the data in the image
class decoded:
    def decode(self):
        img = input("Enter image name(with extension) : ")
        image = Image.open(img, 'r')

        data = ""
        imgdata = iter(image.getdata())

        while (True):
            pixels = [value for value in imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3]]

            # string of binary data
            binstr = ''

            for i in pixels[:8]:
                if (i % 2 == 0):
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if (pixels[-1] % 2 != 0):
                return data

# Main Function
def main():
    a=0
    t1=encoded()

    while(a!=3):
        a = int(input("\n\n-------------------------------\n\n:: Welcome to Steganography ::\n"
                                "1. Encode\n2. Decode\n3. Exit\n"))

        if (a == 1):
            t1.run()


        elif (a == 2):
            t2=decoded()
            message=t2.decode()
            key = input("Enter password: ")
            if(key==t1.getPassword()):
                print("\nDecoded message :  ")
                print(message)
            else:
                print("Wrong Password. Access Denied!")

        elif (a == 3):
            print("Exiting...")

        else:
           raise Exception("Enter correct option")

# Driver Code
if __name__ == '__main__' :

    # Calling main function
    main()