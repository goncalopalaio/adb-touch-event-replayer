package com.gplio.automatorserver

import android.support.test.uiautomator.UiDevice
import android.util.Log
import java.io.PrintStream
import java.net.InetAddress
import java.net.ServerSocket
import java.nio.charset.Charset

/**
* Created by goncalopalaio on 03/02/18.
*/

class ServerRunnable(val ui: UiDevice) : Runnable {
    override fun run() {
        val serverSocket = ServerSocket(PORT);
        val running = true;

        log("starting")

        while (running) {
            log( "accepting connections on server socket: " + serverSocket)
            val socket = serverSocket.accept();

            val t = Thread({
                log("socket connected: " + socket.inetAddress + " " + socket.port)
                val printStream = PrintStream(socket.getOutputStream())

                printStream.print("dumping views from" + ui.currentPackageName)
                ui.dumpWindowHierarchy(printStream)
                printStream.flush()


                /*
                val input = socket.getInputStream()
                val a:ByteArray = kotlin.ByteArray(8192)
                while (input.read(a) > 0) {
                    val str = a.toString(Charset.defaultCharset())
                    socketCallbackInterface.onLineRead(str)

                    printStream.print("echo" + SEP + str)
                    printStream.flush()


                    if (str.indexOf(END)>=0) {
                        break
                    }
                }*/

                printStream.close()
                socket.close()
            })
            t.start()
            t.join()
        }

        log("Stopping")
    }

    private fun log(text: String) {
        if (VERBOSE) {
            Log.d(TAG, text)
        }
    }

    companion object {
        val VERBOSE = false
        val PORT = 9008
        val END = "|"
        val SEP = ","
        val TAG = "ServerSocketRunnable"
    }
}