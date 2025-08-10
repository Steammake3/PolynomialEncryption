from finitefield import GF, isprime

class MSG_Handler:

    BASE97 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+{}|:\"<>?`-=[]\\;',./ Ññ"

    def __init__(self, field = int):
        self.field = field

    def accommodate(self, txt_len, key_len):
        self.field = GF(self.minGF_calc(txt_len, key_len))
        return "Success"

    def minGF_calc(self, txt_len : int, key_len : int):
        n = txt_len*2+key_len
        val = n
        for i in range(int(n), int(2*n)):
            if i%6 in (1,5):
                if isprime(i):
                    val = i
                    break
        return max(97, val)

    def get_val_of_digraph(self, digraph : str):
        BASE97 = MSG_Handler.BASE97
        field = self.field
        return field(BASE97.find(digraph[0])+97*BASE97.find(digraph[1]))

    def get_digraph_of_val(self, val):
        BASE97 = MSG_Handler.BASE97
        return f"{BASE97[val%97]}{BASE97[int(val)//97]}"

    def possibilities(self, char : int):
        """Couldn't find a good name, it basically finds how many distinct
        second characters exist in a diagraph in a field for a given character""" 
        return (self.field.p-char)//97 + 1

    def get_str_of_points(self, points_y : list):
        return ''.join(self.get_digraph_of_val(point) for point in points_y)

    def get_points_of_str(self, txt : str):
        return [self.get_val_of_digraph(txt[s:s+2]) for s in range(0, len(txt), 2)]