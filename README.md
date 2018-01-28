# adb-touch-event-replayer

## Work in progress - For now, this is just a bunch of notes.

Opening screens in your Android application again and again to test an issue is really boring.
Currently there are several tools that might help with this:

* [https://github.com/tzutalin/adb-event-record]
* [https://github.com/xiaocong/uiautomator]
* [https://github.com/appetizerio/replaykit]

From my research:

### adb-event-record

Relies heavily on adb to record the events and replay them.

Records events with: 
```
adb shell getevent
```
Saves the output to file and replays them using:
```
adb shell sendevent
```
Simple and effective.

### uiautomator

This has a really interesting way of working. 
There's an Android UI test framework called UI automator [https://developer.android.com/training/testing/ui-automator.html].
During tests you are able, with this framework, to search and interact with specific View elements, not only in the application you are testing but across all applications, including system settings and whatnot.
So here's the main idea, what about you were always running a UI test?
This tool installs an apk that will run a UI test with UI automator continuously in the background, giving you the ability to search for specific views across all the device. That apk that is installed is also responsible for creating an http server in the Android device that then will receive orders from your local computer. 

### Replaykit
 - Only binaries so I currently don't know the method


# NOTES

Initialy I wanted to implement something similar to adb-event-record but by reading the events directly from /dev/input/event instead of using adb shell getevent. In my search I found this article [http://newandroidbook.com/Book/Input.html?r] that explains really well how everything works internally.

It's from this book: [https://www.amazon.com/gp/product/0991055527]. There's an older version available in the author's website and a new version coming soon.

Details about adb shell getevent: [https://source.android.com/devices/input/getevent#showing-live-events]
Source code here: [http://androidxref.com/8.0.0_r4/xref/system/core/toolbox/getevent.c#673]


