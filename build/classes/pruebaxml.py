import networkx as nx

import chilkat
import xml.etree.ElementTree as ET
import xmltodict
import json
from lxml import etree
import graphviz
import os
import sys

R = nx.DiGraph()

def agregar(nodo):
  for j in nodo:
    #print(j)
    R.add_node(j)
    R.add_edge(nodo,j)
    agregar(j)
    
if __name__=="__main__":
  
  ruta=sys.argv[1]
  nombreaux=sys.argv[2]
  print("nombreaux: "+ nombreaux)
  nombrefinal=nombreaux[0:-5]+".png"
  nombre=nombreaux[0:-5]+".xml"
  print("nombre: "+ nombre)
  ruta2=ruta[0:(len(ruta)-len(sys.argv[2])-1)]
  print(ruta2)
  htmlToXml = chilkat.CkHtmlToXml()

  htmlToXml.put_XmlCharset("utf-8")
  print(ruta,ruta2+"\\"+nombre)
  success = htmlToXml.ConvertFile(ruta,ruta2+"\\"+nombre)
  if (success != True):

      print(htmlToXml.lastErrorText())

  else:

      print("Success")

  doc = etree.parse(ruta2+"\\"+nombre)
  raiz=doc.getroot()
  print (raiz.tag)
  html=raiz[0]

  agregar(raiz)
  nx.write_graphml(R, "nodos.graphml")
  A = nx.nx_agraph.to_agraph(R)
  A.layout('dot')
  A.draw(ruta2+'\\'+nombrefinal) # guardar como png
  
  graphviz.Source(A.to_string()) # mostrar en jupyter