package com.gplio.automatorserver


import android.support.test.InstrumentationRegistry
import android.support.test.runner.AndroidJUnit4
import android.support.test.uiautomator.UiDevice
import android.util.Log
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import java.net.InetAddress


/**
 * Created by goncalopalaio on 04/01/18.
 */
@RunWith(AndroidJUnit4::class)
public class Stub {

    private lateinit var automator: UiDevice


    @Before
    fun setup() {
        automator = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())
        automator.setCompressedLayoutHeirarchy(true);
    }

    @Test
    public fun testActionCountPerSecond() {
        val start = System.currentTimeMillis()
        val totalElements = 10;

        for (i in 0..totalElements) {
            Log.d(TAG, "I'm alive")
            automator.click(120, 370);
            automator.pressHome()
        }

        Log.d(TAG, "Time to process: " + totalElements + " seconds:" + (System.currentTimeMillis()-start)/1000f  )
    }
   @Test
    public fun keepServerAlive() {
       Thread(SocketRunnable(object: SocketCallback {
           override fun onStart() {
           }

           override fun onSocketConnected(inetAddress: InetAddress, port: Int) {
           }
       } )).run();

       val alive = true
        while (alive)
            Log.d(TAG, "I'm alive")
            Thread.sleep(100)
    }

    companion object {
        val TAG = "Stub"
    }
}