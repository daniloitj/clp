import os, Image,ImageDraw, ImageFilter, time

class Imagem:
    local_de_entrada = None
    local_de_saida = None
    imagens_de_entrada = None	
    imagem_com_filtro = None
    vetor = []

    def __init__(self):
        self.local_de_entrada = "C:\Users\HP\Desktop\imagens\inputFolder"
        self.local_de_saida = "C:\Users\HP\Desktop\imagens\outFolder"
        self.vetor = []		
        print "Criando nova instancia Imagem" 

    def aplica_filtro(self):
        self.imagens_de_entrada = os.listdir(self.local_de_entrada)
        t0 = time.clock()
        for file in self.imagens_de_entrada:
            self.imagem_com_filtro = self.local_de_entrada + "\\" + file
            im = Image.open(self.imagem_com_filtro).convert("L")
            width, height = im.size
            print im.format, im.size, im.mode, width, height
            fil = im.filter(ImageFilter.FIND_EDGES)		
        self.imagem_com_filtro = self.local_de_saida + "\\" + file
        fil.save(self.imagem_com_filtro)
        tempo_final = t0 - time.clock()	
        return 0
		
    def criar_imagem(self,x,y):
        img = Image.new("RGB", (x,y), "#FFFFFF")
        draw = ImageDraw.Draw(img)
        img.save(self.local_de_saida + "/out.png", "PNG")
        return img
		
    def vetor_de_img(self, tamanho_do_vetor):
        x = self.criar_imagem(3,3)
        t0 = time.clock()
        for y in range(1,tamanho_do_vetor):
            self.vetor.append(x)
        tempo_final = t0 - time.clock()
        print tempo_final
        return 0 
 

	

	
