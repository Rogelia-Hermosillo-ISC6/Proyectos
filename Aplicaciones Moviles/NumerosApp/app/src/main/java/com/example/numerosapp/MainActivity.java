package com.example.numerosapp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Button btnPrimos, btnPerfectos, btnAmigos;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnPrimos = findViewById(R.id.btnPrimos);
        btnPerfectos = findViewById(R.id.btnPerfectos);
        btnAmigos = findViewById(R.id.btnAmigos);

        btnPrimos.setOnClickListener(v ->
                startActivity(new Intent(this, Primos.class)));

        btnPerfectos.setOnClickListener(v ->
                startActivity(new Intent(this, Perfectos.class)));

        btnAmigos.setOnClickListener(v ->
                startActivity(new Intent(this, Amigos.class)));
    }
}