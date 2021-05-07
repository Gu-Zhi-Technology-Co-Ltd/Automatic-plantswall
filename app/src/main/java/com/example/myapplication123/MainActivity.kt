package com.example.myapplication123
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

    }
    val host = "192.168.8.104"
    val port = 8081
    var sum = ""

    fun  show(sum:String){
        val textView: TextView =  findViewById(R.id.textView)
        textView.text = sum.toString()

    }

    fun press(@Suppress("UNUSED_PARAMETER")view: View) {
        Thread(Runnable {
            //Thread.sleep(1000)
            //while (true) {
            //show("222")
            sum = ClientSo(host, port).run().toString()

            //}
        }).start()
        show(sum)
    }
    fun test(view: View){

    }
    //fun click(view: View) {

    //}
    //fun sds(view: View) {
    //show(sum)
    //}
}