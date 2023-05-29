def MergeSort(array):
    if len(array) > 1:

        middle = len(array) // 2 # Dizinin iki parçaya ayırılma işlemi
        LeftSide = array[:middle] # Dizinin 0.İndexten middle indexsine kadar ki kısma ayırılmaıs
        RightSide = array[middle:] # Dizinin middle'dan sonuncu indexe kadar ayırılması

        MergeSort(LeftSide)
        MergeSort(RightSide)
        mergeSort(array, LeftSide, RightSide)


def mergeSort(array, LeftSide, RightSide):
    LeftC = 0 # Kontrol değerleri
    RightC = 0 # Kontrol değerleri
    MergeC = 0 # Kontrol değerleri

    """
    Bu kontrol değerlerinin amacı dizimizin içerisindeki indexlere erişebilmektir.
    """

    while LeftC < len(LeftSide) and RightC < len(RightSide):
        """
        Sol ve Sağ olarak ayırdığımız parçaların kalansız ayrıştığını kontrol ediyoruz.
        """
        if LeftSide[LeftC] < RightSide[RightC]:
            """
            Dizinin sol tarafındaki 0.değer sağ tarafındaki 0.değerden küçük ise
            """

            array[MergeC] = LeftSide[LeftC]
            LeftC = LeftC + 1

            """
            Sol tarafın 0.değerini dizinin 0.değerine eşitliyoruz
            Artık bir sonraki index'e bakmak istediğimizden sol tarafın kontrol index'ine 
            (Yeni)Sayı = (Eski) sayı + 1 
            """

        else:
            """
            Dizinin sol tarafındaki 0.değer sağ tarafındaki 0.değerden küçük değil ise
            """
            array[MergeC] = RightSide[RightC]
            RightC = RightC + 1

            """
            Sağ tarafın 0.değerini dizinin 0.değerine eşitliyoruz
            Artık bir sonraki index'e bakmak istediğimizden Sağ tarafın kontrol index'ine 
            (Yeni)Sayı = (Eski) sayı + 1
            """

        MergeC = MergeC + 1
        """
        Dizimizin kontrol işlemini 0.indexten yani ilk değerden başlatmıştık 
        Yukarıda yaptığımız işlemler sonucunda ilk değere atama yaptığımız ve bir sonraki 
        değere geçmemiz gerektiğinden index değerini arttırmamız gerekmektedir.
        (Yeni)Sayı = (Eski) sayı + 1
        """

    while LeftC < len(LeftSide):
        """
        LeftC değerimiz 0'dı. Bu değeri indexler arası geçişte kullanıyorduk.
        şimdi ise sol tarafın tamamen parçalarına ayırılıp ayırılmadığını kontrol etmek
        için kullanıyoruz.    
        """
        array[MergeC] = LeftSide[LeftC]
        LeftC = LeftC + 1
        MergeC = MergeC + 1
        """
        Dizimizin indext değerini sol tarafın index değerine eşitleyerek atamasını
        yapıyoruz. 
        Ve yine bir sonraki indexi kontrol etmek için index değerlerini 1 arttırıyoruz.
        """

    while RightC < len(RightSide):
        """
        LeftC değerimiz 0'dı. Bu değeri indexler arası geçişte kullanıyorduk.
        şimdi ise sol tarafın tamamen parçalarına ayırılıp ayırılmadığını kontrol etmek
        için kullanıyoruz.  
        """
        array[MergeC] = RightSide[RightC]
        MergeC = MergeC + 1
        RightC = RightC + 1
        """
        Dizimizin indext değerini sol tarafın index değerine eşitleyerek atamasını
        yapıyoruz.
        Ve yine bir sonraki indexi kontrol etmek için index değerlerini 1 arttırıyoruz.
        """



List = [16, 21, 11, 8, 12, 22]

MergeSort(List)
print(List)

