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
        >>> y = Imagem()
        >>> y.vetor_de_img(2)
		

    """
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
        """cria um vetor do tamanho do argumento que recebe, e retorna o tempo nescessario para armazenar essas imagens

        :Example:

        >>> import Imagem
        >>> a = Imagem.vetor_de_img(300)

        """	
        x = self.criar_imagem(3,3)
        t0 = time.clock()
        for y in range(1,tamanho_do_vetor):
            self.vetor.append(x)
        tempo_final = t0 - time.clock()
        return tempo_final 
 

	

	
