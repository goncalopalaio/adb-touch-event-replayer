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
class Server {

    private lateinit var automator: UiDevice

    @Before
    fun setup() {
        automator = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())
        automator.setCompressedLayoutHeirarchy(true);
    }

    @Test
    fun runServer() {
        // No apk changes detected since last installation, skipping installation of /Users/goncalopalaio/Dropbox/2017/adb-touch-event-replayer/AutomatorServer/app/build/outputs/apk/debug/app-debug.apk
        // $ adb shell am force-stop com.gplio.automatorserver
        // $ adb push /Users/goncalopalaio/Dropbox/2017/adb-touch-event-replayer/AutomatorServer/app/build/outputs/apk/androidTest/debug/app-debug-androidTest.apk /data/local/tmp/com.gplio.automatorserver.test
        // $ adb shell pm install -t -r "/data/local/tmp/com.gplio.automatorserver.test"
        // adb shell am instrument -w -r   -e debug false -e class com.gplio.automatorserver.Server com.gplio.automatorserver.test/android.support.test.runner.AndroidJUnitRunner
        val t = Thread(ServerRunnable(automator))
        t.start()
        t.join()
        Log.d("ServerAndroidTest", "@Test exiting")
    }
}