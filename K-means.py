# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:27:53 2021

@author: Clara
"""
import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets as sk
import random 

class K_means():
    """Classe que implementa o método K-means
    """
    def __init__(self,k=3):
        self.set_obs()
        self.criar_centroide(k)
        
    def set_obs(self,n_centroid=3):
        """
        Cria as observacoes já separadas num numero de clusters específicados pelo usuário.

        Parameters
        ----------
        k : INT, optional
            NÚMERO DE CLUSTERS A SEREM CRIADOS. The default is 3.

        Returns
        -------
        None.

        """
        self.observacoes,y = sk.make_blobs(n_samples=100, centers=n_centroid, random_state=101)

    def set_centroide(self,k):
        """
        Escolhe aleatóriamente os centroides a partir dos dados.
        
        Parameters
        ----------
        k : INT
           Número de clesters a serem criados.

        Returns
        -------
        None.

        """
        #cria vetor com os valores dos indices dos pontos 
        index = range(len(self.observacoes))
       
        self.centroids = self.observacoes[random.sample(index,k)]

        #print(self.centroids)

    def normaeuclideana(dado,k):
        pass

    def indexardados(dados):
        pass

dado = K_means()

#print(dado.observacoes)