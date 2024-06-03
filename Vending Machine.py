import sys
import cv2
import numpy as np
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

class ShowImage(QMainWindow):
    def __init__(self):
        super(ShowImage, self).__init__()
        loadUi('Vending Machine.ui', self)

        # Inisialisasi variabel
        self.Image = None
        self.item_counts = {
            "Coca Cola": 0,
            "Sprite": 0,
            "Tebs": 0,
            "Aqua": 0,
            "Nescafe": 0,
            "Lasegar": 0
        }

        self.item_prices = {
            "Coca Cola": 10000,
            "Sprite": 10000,
            "Tebs": 7000,
            "Aqua": 5000,
            "Nescafe": 7000,
            "Lasegar": 7000
        }

        self.total_price = 0
        self.detected_value = 0

        # Menghubungkan tombol dengan metode yang sesuai
        self.cola_Beli.clicked.connect(self.colabeli)
        self.sprite_Beli.clicked.connect(self.spritebeli)
        self.tebs_Beli.clicked.connect(self.tebsbeli)
        self.aqua_Beli.clicked.connect(self.aquabeli)
        self.nescafe_Beli.clicked.connect(self.nescafebeli)
        self.lasegar_Beli.clicked.connect(self.lasegarbeli)
        self.deteksi_btn_2.clicked.connect(self.deteksi_koin)
        self.deteksi_btn.clicked.connect(self.deteksi_kertas)
        self.respesan_btn.clicked.connect(self.reset_pesan)
        self.ressaldo_btn.clicked.connect(self.reset_saldo)
        self.bayar_btn.clicked.connect(self.bayar)

    # Metode untuk mendeteksi koin pada gambar


        self.update_list_widget("Sprite")

    # Metode untuk membeli Tebs
    def tebsbeli(self):
        if not self.textBrowser_2.toPlainText().strip():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Masukan Uang Terlebih Dahulu")
            msg.setStyleSheet(
                "QMessageBox { background-color: white; color: black; } QPushButton { background-color: blue; color: white; }")
            msg.setText("Masukan uang terlebih dahulu sebelum membeli.")
            msg.exec_()
            return

        self.update_list_widget("Tebs")

    # Metode untuk membeli Aqua
    def aquabeli(self):
        if not self.textBrowser_2.toPlainText().strip():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Masukan Uang Terlebih Dahulu")
            msg.setStyleSheet(
                "QMessageBox { background-color: white; color: black; } QPushButton { background-color: blue; color: white; }")
            msg.setText("Masukan uang terlebih dahulu sebelum membeli.")
            msg.exec_()
            return

        self.update_list_widget("Aqua")

    # Metode untuk membeli Nescafe
    def nescafebeli(self):
        if not self.textBrowser_2.toPlainText().strip():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Masukan Uang Terlebih Dahulu")
            msg.setStyleSheet(
                "QMessageBox { background-color: white; color: black; } QPushButton { background-color: blue; color: white; }")
            msg.setText("Masukan uang terlebih dahulu sebelum membeli.")
            msg.exec_()
            return

        self.update_list_widget("Nescafe")

    # Metode untuk membeli Lasegar
    def lasegarbeli(self):
        if not self.textBrowser_2.toPlainText().strip():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Masukan Uang Terlebih Dahulu")
            msg.setStyleSheet(
                "QMessageBox { background-color: white; color: black; } QPushButton { background-color: blue; color: white; }")
            msg.setText("Masukan uang terlebih dahulu sebelum membeli.")
            msg.exec_()
            return

        self.update_list_widget("Lasegar")

    # Metode untuk mereset pesan pembelian
    def reset_pesan(self):
        self.listWidget.clear()
        self.textBrowser.clear()
        self.total_price = 0
        for item in self.item_counts:
            self.item_counts[item] = 0

    # Metode untuk mereset pesan nominal uang
    def reset_saldo(self):
        self.textBrowser_2.clear()
        self.detected_value = 0

    # Metode untuk proses pembayaran


app = QtWidgets.QApplication(sys.argv)
window = ShowImage()
window.setWindowTitle('Vending Machine')
window.show()
sys.exit(app.exec_())

