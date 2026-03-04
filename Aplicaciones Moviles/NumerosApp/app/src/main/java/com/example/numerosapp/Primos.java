package com.example.numerosapp;

import android.os.Bundle;
import android.content.Intent;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

public class Primos extends AppCompatActivity {

    EditText etNumero;
    Button btnVerificar;
    TextView tvResultado;
    ImageButton btnAtras, btnSiguiente;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_primos);

        etNumero = findViewById(R.id.etNumero);
        btnVerificar = findViewById(R.id.btnVerificar);
        tvResultado = findViewById(R.id.tvResultado);

        btnAtras = findViewById(R.id.btnAtras);
        btnSiguiente = findViewById(R.id.btnSiguiente);

        // 🔹 Lógica número primo
        btnVerificar.setOnClickListener(v -> {

            if (etNumero.getText().toString().isEmpty()) {
                Toast.makeText(this, "Ingresa un número", Toast.LENGTH_SHORT).show();
                return;
            }

            int num = Integer.parseInt(etNumero.getText().toString());
            boolean esPrimo = true;

            if (num <= 1) esPrimo = false;

            for (int i = 2; i < num; i++) {
                if (num % i == 0) {
                    esPrimo = false;
                    break;
                }
            }

            if (esPrimo)
                tvResultado.setText("Es número primo");
            else
                tvResultado.setText("No es número primo");
        });

        // 🔙 Flecha izquierda → volver al menú principal
        btnAtras.setOnClickListener(v -> finish());

        // ➡ Flecha derecha → ir a Perfectos
        btnSiguiente.setOnClickListener(v ->
                startActivity(new Intent(this, Perfectos.class)));
    }
}