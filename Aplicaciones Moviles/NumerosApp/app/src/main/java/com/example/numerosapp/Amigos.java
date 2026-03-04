package com.example.numerosapp;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.content.Intent;
import android.widget.*;

public class Amigos extends AppCompatActivity {

    EditText etNumero1, etNumero2;
    Button btnVerificar;
    TextView tvResultado;
    ImageButton btnAtras, btnSiguiente;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_amigos);

        etNumero1 = findViewById(R.id.etNumero1);
        etNumero2 = findViewById(R.id.etNumero2);
        btnVerificar = findViewById(R.id.btnVerificar);
        tvResultado = findViewById(R.id.tvResultado);

        btnAtras = findViewById(R.id.btnAtras);
        btnSiguiente = findViewById(R.id.btnSiguiente);

        // 🔹 Lógica números amigos
        btnVerificar.setOnClickListener(v -> {

            if (etNumero1.getText().toString().isEmpty() ||
                    etNumero2.getText().toString().isEmpty()) {

                Toast.makeText(this, "Ingresa ambos números", Toast.LENGTH_SHORT).show();
                return;
            }

            int n1 = Integer.parseInt(etNumero1.getText().toString());
            int n2 = Integer.parseInt(etNumero2.getText().toString());

            int suma1 = 0;
            int suma2 = 0;

            for (int i = 1; i < n1; i++)
                if (n1 % i == 0)
                    suma1 += i;

            for (int i = 1; i < n2; i++)
                if (n2 % i == 0)
                    suma2 += i;

            if (suma1 == n2 && suma2 == n1)
                tvResultado.setText("Son números amigos");
            else
                tvResultado.setText("No son números amigos");
        });

        btnAtras.setOnClickListener(v ->
                startActivity(new Intent(this, Perfectos.class)));

        btnSiguiente.setOnClickListener(v ->
                startActivity(new Intent(this, MainActivity.class)));
    }
}