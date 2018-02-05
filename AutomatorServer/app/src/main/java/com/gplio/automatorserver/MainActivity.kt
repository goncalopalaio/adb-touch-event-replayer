package com.gplio.automatorserver

import android.annotation.SuppressLint
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView
import java.net.InetAddress

class MainActivity : AppCompatActivity() {
    private lateinit var tvLog:TextView
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        tvLog = findViewById<TextView>(R.id.tv_log)


        for (i in 0..10) {
            log("Hello " + i)
        }

        Thread(SocketRunnable(object: SocketCallback {
            override fun onStart() {
                log("Started socket")
            }

            override fun onSocketConnected(inetAddress: InetAddress, port: Int) {
                log("Socket connected")
            }

            override fun onLineRead(str: String) {
                log("Line: " + str)
            }
        })).start()
    }

    @SuppressLint("SetTextI18n")
    private fun log(text: String) {
        tvLog.text = text + "\n" + tvLog.text
    }
}
