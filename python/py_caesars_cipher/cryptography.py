# encryption
# self.char = "`~.q,wmenrbtvcyxuziaospd[f]g'h;jl k+=_-)(09*8&7^6%5$$#3@2!1MQNWBEVRCTYZXIOASPUDFLKGJH"

class Caesars_Shift():
    def __init__(self, char):
        self.char = char
        self.char_array = [x for x in char]
        self.enc_msg = ""
        self.dec_msg = ""
        self.index1 = 0
        self.index2 = 0

    def encrypt_message(self):
        enc_msg_array = []

        def prompt_user_inputs():
            self.msg = input("Enter_message: ")
            self.key = int(input("Key: "))

        def create_arrays():
            self.msg_array = [x for x in self.msg]

        prompt_user_inputs()
        create_arrays()

        for i in self.msg:
            self.index2 = 0
            for j in self.char:
                if i == j:
                    enc_msg_array.append(self.char_array[self.index2+self.key])
                self.index2 += 1
            self.index1 += 1

        for i in enc_msg_array:
            self.enc_msg += i

    def get_encrypted_message(self):
        print(self.enc_msg)

    def decrypt_message(self):
        dec_msg_array = []

        for i in self.enc_msg:
            self.index2 = 0
            for j in self.char:
                if i == j:
                    dec_msg_array.append(self.char_array[self.index2-self.key])
                self.index2 += 1
            self.index1 += 1

        for i in dec_msg_array:
            self.dec_msg += i

    def get_decrypted_message(self):
        print(self.dec_msg)
