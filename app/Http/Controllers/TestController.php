<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class TestController extends Controller
{
    public function verificarRuta()
    {
        $response = Http::get('http://localhost/test'); // Cambia la URL según tu entorno

        if ($response->status() === 200) {
            return "La respuesta tiene un código 200.";
        } else {
            return "La respuesta no tiene un código 200.";
        }
    }
}
