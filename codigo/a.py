import os, Image,ImageDraw, ImageFilter, time

class Imagem:
    """Crie uma instancia dessa classe e podera: 
          :criar um vetor de imagens do tamanho permitido pela limite da sua maquina: description
          :aplicar um filtro em uma imagem: description
          :criar uma imagem em branco: type description
     

    - **parameters**, **types**, **return** and **return types**::

          :param local_de_entrada: contem o endereco de uma pasta, a qual se pode adicionar imagens e aplicar filtros
          :param local_de_saida: contem o endereco de uma pasta, a qual vai conter o resultado dos filtros
          :param imagens_de_entrada: aqui armazeno todas as imagens que estao na pasta de entrada
          :param imagem_com_filtro: destinado a armazenar as imagens com filtros
          :param vetor: para armazenar as imagens em uma lista
		  

    - **Examplo de Como usar:**::

        :Examplo de Como usar::

        >>> import Imagem
        >>> y = Imagem(tamanho da imagem que vai querer testar)
        >>> y.vetor_de_img(2)
		

    """
    local_de_entrada = None
    local_de_saida = None
    imagens_de_entrada = None	
    imagem_com_filtro = None
    vetor = []
    tupla = ()
    tam_img = None

    def __init__(self, tam_img):
        self.local_de_entrada = "C:\Users\HP\Desktop\imagens\inputFolder"
        self.local_de_saida = "C:\Users\HP\Desktop\imagens\outFolder"
        self.vetor = []	
        self.tupla = ()
        self.tam_img = tam_img		

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
		
    def vetor_de_img(self, tamanho):
        """cria um vetor do tamanho do argumento que recebe, e retorna o tempo nescessario para armazenar essas imagens

        :Example:

        >>> import a
        >>> t = a.Imagem(300)
        >>> t = t.vetor_de_img(9)
        >>> 0

        """	
        x = self.criar_imagem(self.tam_img,self.tam_img)
        self.vetor=[]
        t0 = time.clock()
        for y in range(1,tamanho):
            self.vetor.append(x)
        tempo_final = t0 - time.clock()
        t1 = time.time()
        for y in range(1,tamanho):
            self.vetor.append(x)
        t2 = time.time()
        print "|vet.\t  |%d   \t\t|%2.7fs             |%2.7fs" %(tamanho, t2 - t1, tempo_final) 		
        return 0 
 

    def list_comprehension_de_img(self, tamanho):
        """Usando list_comprehension do tamanho do argumento que recebe, e retorna o tempo nescessario para armazenar essas imagens

        :Example:

        >>> import Imagem
        >>> a = Imagem.list_comprehension_de_img(300)
        >>> 0

        """	
        x = self.criar_imagem(self.tam_img,self.tam_img)
        numeros = range(tamanho)
        t0 = time.clock()
        lista = [x for y in numeros]
        tempo_final = t0 - time.clock()
        t1 = time.time()
        lista = [x for y in numeros]
        t2 = time.time()
        print "|l.c.\t  |%d   \t\t|%2.7fs             |%2.7fs" %(tamanho, t2 - t1, tempo_final) 
        return 0	

    def tupla_img(self, tamanho):
        """cria um tupla do tamanho do argumento que recebe, e retorna o tempo nescessario para armazenar essas imagens

        :Example:

        >>> import Imagem
        >>> a = Imagem.tupla(300)
        >>> 0

        """	
        x = self.criar_imagem(self.tam_img,self.tam_img)
        self.tupla = ([],)
        t0 = time.clock()
        for y in range(1,tamanho):
            self.tupla[0].append(x)
        tempo_final = t0 - time.clock()
        t1 = time.time()
        for y in range(1,tamanho):
            self.tupla[0].append(x)
        t2 = time.time()
        print "|tup.\t  |%d   \t\t|%2.7fs             |%2.7fs" %(tamanho, t2 - t1, tempo_final) 
        return 0	
		
    def matrix_de_img(self, tamanho):
        """cria uma matrix do tamanho do argumento que recebe, e retorna o tempo nescessario para armazenar essas imagens

        :Example:

        >>> import Imagem
        >>> a = Imagem.vetor_de_img(k,k)
        >>> 0

        """	
        linha = tamanho
        x = self.criar_imagem(self.tam_img,self.tam_img)
        t1 = time.time()
        list(list(x for i in range(linha)) for j in range(1))
        t2 = time.time()
        t0 = time.clock()
        list(list(x for i in range(linha)) for j in range(1))
        tempo_final = t0 - time.clock()
        print "|mat.\t  |%d   \t\t|%2.7fs             |%2.7fs" %(tamanho, t2 - t1, tempo_final)
        return 0		
		
		
print "\n\n|func.    |Quant.\t\t|(tempo real) \t\t|(tempo cpu)"
y = Imagem(300)
k = 90000
y.list_comprehension_de_img(k)
y.vetor_de_img(k)
y.tupla_img(k)
y.matrix_de_img(k)
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
"""