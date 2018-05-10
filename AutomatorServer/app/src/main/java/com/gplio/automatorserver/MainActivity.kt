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
        tvLog.setText("Nothing to see here")
    }
}
