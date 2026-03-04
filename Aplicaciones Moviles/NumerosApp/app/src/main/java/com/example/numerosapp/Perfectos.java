package com.example.numerosapp;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.content.Intent;
import android.widget.*;
import android.view.View;

public class Perfectos extends AppCompatActivity {

    EditText etNumero;
    Button btnVerificar;
    TextView tvResultado;
    ImageButton btnAtras, btnSiguiente;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_perfectos);

        etNumero = findViewById(R.id.etNumero);
        btnVerificar = findViewById(R.id.btnVerificar);
        tvResultado = findViewById(R.id.tvResultado);

        btnAtras = findViewById(R.id.btnAtras);
        btnSiguiente = findViewById(R.id.btnSiguiente);

        // 🔹 LÓGICA NÚMERO PERFECTO
        btnVerificar.setOnClickListener(v -> {

            if (etNumero.getText().toString().isEmpty()) {
                Toast.makeText(this, "Ingresa un número", Toast.LENGTH_SHORT).show();
                return;
            }

            int num = Integer.parseInt(etNumero.getText().toString());
            int suma = 0;

            for (int i = 1; i < num; i++) {
                if (num % i == 0) {
                    suma += i;
                }
            }

            if (suma == num)
                tvResultado.setText("Es número perfecto");
            else
                tvResultado.setText("No es número perfecto");
        });

        // 🔙 Ir a Primos
        btnAtras.setOnClickListener(v -> {
            startActivity(new Intent(this, Primos.class));
            finish();
        });

        // ➡ Ir a Amigos
        btnSiguiente.setOnClickListener(v -> {
            startActivity(new Intent(this, Amigos.class));
            finish();
        });
    }
}