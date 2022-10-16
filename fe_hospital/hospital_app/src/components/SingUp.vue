<template>
  <div class="signUp_user">
    <div class="container_signUp_user">
      <h2>Registrarse</h2>
      <form v-on:submit.prevent="processSignUp">
        <input type="text" v-model="user.username" placeholder="Username" />
        <br />
        <input type="password" v-model="user.password" placeholder="Password" />
        <br />
        <select type="text" v-model="user.perfil" name="Rol" class="select_rol">
          <option value="" disabled selected>Perfil</option>
          <option value="Medico">Medico</option>
          <option value="Paciente">Paciente</option>
          <option value="Familiar">Familiar</option>
          <option value="Auxiliar">Auxiliar</option>
        </select>
        <br />
        <input type="text" v-model="user.nombre" placeholder="Nombre" />
        <br />
        <input type="text" v-model="user.apellidos" placeholder="Apellidos" />
        <br />
        <input type="text" v-model="user.telefono" placeholder="Telefono" />
        <br />
        <select
          type="text"
          v-model="user.genero"
          name="genero"
          class="select_genero"
        >
          <option value="" disabled selected>Genero</option>
          <option value="Femenino">Femenino</option>
          <option value="Masculino">Masculino</option>
          <option value="No_definido">No definido</option>
        </select>
        <br />
        <button type="submit">Registrarse</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SignUp",
  data: function () {
    return {
      user: {
        username: "",
        password: "",
        perfil: "",
        nombre: "",
        apellidos: "",
        telefono: "",
        genero: "",
      },
    };
  },
  methods: {
    processSignUp: function () {
      axios
        .post("http://127.0.0.1:8000/usercrear/", this.user, { headers: {} })
        .then((result) => {
          let dataSignUp = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };

          this.$emit("completedSignUp", dataSignUp);
        })
        .catch((error) => {
          console.log(error);
          alert("Registro Exitoso");
        });
    },
  },
};
</script>

<style>
.signUp_user {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container_signUp_user {
  border: 3px solid #283747;
  border-radius: 10px;
  width: 35%;
  height: 130%;
  background: #e5e7e9;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.signUp_user h2 {
  color: #283747;
}

.signUp_user form {
  width: 70%;
}

.signUp_user input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #283747;
}

.signUp_user button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}

.signUp_user button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 1px solid #283747;
}

.select_rol {
  color: #283747;
  width: 100%;
  height: 40px;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #283747;
}

.select_rol option {
  color: black;
  font-size: 14px;
}

.select_genero {
  color: #283747;
  width: 100%;
  height: 40px;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #283747;
}

.select_genero option {
  color: black;
  font-size: 14px;
}
</style>
