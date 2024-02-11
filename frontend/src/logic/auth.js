import axios from "axios";
import {API_PATH}  from "@/logic/entorno.js";


const auth = {

  //  Validación y login de usuarios
  async login(username, password) {
    const user = { username, password };
    try {
      const response = await axios.post(API_PATH + "users/token/", user);
      return response; // Devuelve la respuesta
    } catch (error) {
      throw error;
    }
  },

  // Cierre de sesión de usuario
  async logout(accessToken, refreshToken) {
    try {
      const data = { refresh: refreshToken };
      const response = await axios.post(API_PATH + "users/logout/", data, {
        headers: {
          Authorization: `Bearer ${accessToken}` // Pasar el token de acceso en el encabezado de autorización
        }
      });
      return response; // Devuelve la respuesta
    } catch (error) {
      console.error("Error en la solicitud:", error.config); // Imprimir la configuración de la solicitud
      throw error;
    }
  },

  // Función para verificar si el usuario está autenticado
  isAuthenticated() {
    // Verificar si hay un token de acceso almacenado en el localStorage
    const accessToken = sessionStorage.getItem("access_token");
    // Devolver true si el token de acceso existe
    return !!accessToken;
  },


  
};

export default auth;
