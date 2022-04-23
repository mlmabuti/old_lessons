from cryptography import Caesars_Shift as cs

characters = (
    "`~.q,wmenrbtvcyxuziaospd[f]g'h;jl k+=_-)(09*8&7^6%5$$#3@2!1MQNWBEVRCTYZXIOASPUDFLKGJH")
#characters = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM qwertyuiopasdfghjklzxcvbnm"

neu_email = cs(characters)
neu_email.encrypt_message()
neu_email.get_encrypted_message()

neu_email.decrypt_message()
neu_email.get_decrypted_message()
