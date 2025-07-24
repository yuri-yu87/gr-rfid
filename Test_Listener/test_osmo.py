from gnuradio import gr, qtgui
from PyQt5 import Qt
import sys, osmosdr, sip

class test(gr.top_block, Qt.QWidget):
    def __init__(self):
        gr.top_block.__init__(self, "Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Test")
        self.top_layout = Qt.QVBoxLayout(self)
        self.sink = qtgui.time_sink_c(1024, 1e6, "Test", 1)
        self.src = osmosdr.source(args="hackrf=0")
        self.src.set_sample_rate(1e6)
        self.src.set_center_freq(920e6, 0)
        self.connect(self.src, self.sink)
        self._sink_win = sip.wrapinstance(self.sink.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._sink_win)

if __name__ == '__main__':
    app = Qt.QApplication(sys.argv)
    tb = test()
    tb.start()
    tb.show()
    app.exec_()
    tb.stop()
    tb.wait()
