package com.gplio.automatorserver

import android.util.Log
import java.io.PrintStream
import java.net.InetAddress
import java.net.ServerSocket
import java.nio.charset.Charset

/**
 * Created by goncalopalaio on 03/02/18.
 */

class SocketRunnable(val socketCallbackInterface: SocketCallback) : Runnable {
    override fun run() {
        val serverSocket = ServerSocket(PORT);
        val running = true;
        var count = 0

        socketCallbackInterface.onStart()

        while (running) {
            val socket = serverSocket.accept();
            Log.d(TAG, "Socket: " + socket.inetAddress + " " + socket.port)

            socketCallbackInterface.onSocketConnected(socket.inetAddress, socket.port)

            val input = socket.getInputStream()
            val a:ByteArray = kotlin.ByteArray(8192)

            val printStream = PrintStream(socket.getOutputStream())

            while (input.read(a) > 0) {
                val str = a.toString(Charset.defaultCharset())
                socketCallbackInterface.onLineRead(str)

                printStream.print("echo" + SEP + str)
                printStream.flush()


                if (str.indexOf(END)>=0) {
                    break
                }
            }

            printStream.close()
            count += 1
        }

    }
    private fun parseInstructions() {
        
    }
    companion object {
        val PORT = 9008
        val END = "|"
        val SEP = ","
        val TAG = "SocketRunnable"
    }
}

data class Instruction(val name: String, val param1: String, val param2: String)

interface SocketCallback {
    fun onStart() {
        Log.d(SocketRunnable.TAG, "Start")
    }
    fun onSocketConnected(inetAddress: InetAddress, port: Int) {
        Log.d(SocketRunnable.TAG, "Socket connected: " + inetAddress + " " + port)
    }
    fun onLineRead(str: String) {
        Log.d(SocketRunnable.TAG, "OnLineRead: " + str)
    }
}