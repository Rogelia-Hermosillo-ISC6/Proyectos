package com.example.myfirstapp;

import android.os.Bundle;
import android.app.Activity;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.content.Intent;

public class MainActivity extends Activity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Referencias a los controles
        final EditText txtNombre = (EditText) findViewById(R.id.TxtNombre);
        final Button btnHola = (Button) findViewById(R.id.BtnHola);

        final Button btnMeses = (Button) findViewById(R.id.BtnMeses);
        final EditText txtEdad = (EditText) findViewById(R.id.TxtEdad);
        final EditText txtMeses = (EditText) findViewById(R.id.TxtMeses);

        // Evento botón Hola
        btnHola.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {

                // Creamos el Intent
                Intent intent = new Intent(MainActivity.this, Greeting.class);

                // Creamos la información a pasar
                Bundle b = new Bundle();
                b.putString("NOMBRE", txtNombre.getText().toString());

                // Añadimos la información al intent
                intent.putExtras(b);

                // Iniciamos la nueva actividad
                startActivity(intent);
            }
        });

        // Evento botón Meses
        btnMeses.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {

                String edad = txtEdad.getText().toString();
                int ed = Integer.parseInt(edad);
                String mes = Integer.toString(ed * 12);
                txtMeses.setText(mes);
            }
        });
    }
}
