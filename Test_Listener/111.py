from gnuradio import gr, analog, blocks, qtgui
from PyQt5 import Qt
import sys
import sip

class test(gr.top_block, Qt.QWidget):
    def __init__(self):
        gr.top_block.__init__(self, "Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Test")
        self.top_layout = Qt.QVBoxLayout(self)
        self.sink = qtgui.time_sink_f(1024, 1000, "Test", 1)
        src = analog.sig_source_f(1000, analog.GR_COS_WAVE, 10, 1)
        throttle = blocks.throttle(gr.sizeof_float, 1000)
        self.connect(src, throttle, self.sink)
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