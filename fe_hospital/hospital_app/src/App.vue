<template>
  <div id="app" class="app">
    <div class="header">
      <h1>Hospital en Casa Misión Tic 2022</h1>
      <nav>
        <button v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadSignUp">Registrarse</button>
        <button v-if="is_auth" v-on:click="loadHome">Inicio</button>
        <button v-if="is_auth" v-on:click="loadRequestUser">
          Consultar Usuario
        </button>
        <button v-if="is_auth" v-on:click="loadDeleteUser">
          Eliminar Usuario
        </button>
        <button v-if="is_auth" v-on:click="loadPutUser">
          Modificar Usuario
        </button>
        <button v-if="is_auth" v-on:click="loadPostpsalud">
          Registro Personal
        </button>
        <button v-if="is_auth" v-on:click="loaddeletepsalud">
          Eliminar Personal
        </button>
        <button v-if="is_auth" v-on:click="loadgetpsalud">
          Consulta Personal
        </button>
        <button v-if="is_auth" v-on:click="loadputpsalud">
          Modificar Personal
        </button>
        <button v-if="is_auth" v-on:click="logOut">Cerrar Sesión</button>
      </nav>
      <div>
        <img src="./assets/Medic.png" alt="logo" />
      </div>
    </div>
    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:logOut="logOut"
        v-on:loadRequestUser="loadRequestUser"
        v-on:loadDeleteUser="loadDeleteUser"
        v-on:loadPutUser="loadPutUser"
        v-on:loadPostpsalud="loadPostpsalud"
        v-on:loaddeletepsalud="loaddeletepsalud"
        v-on:loadgetpsalud="loadgetpsalud"
        v-on:loadputpsalud="loadputpsalud"
      >
      </router-view>
    </div>
    <div class="footer">
      <h2>BAJA Scrum/MisiónTic 2022</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data: function () {
    return {
      is_auth: false,
    };
  },
  components: {},

  methods: {
    verifyAuth: function () {
      this.is_auth = localStorage.getItem("isAuth") || false;
      if (this.is_auth == false) this.$router.push({ name: "logIn" });
      else this.$router.push({ name: "Home" });
    },
    loadLogIn: function () {
      this.$router.push({ name: "logIn" });
    },
    loadSignUp: function () {
      this.$router.push({ name: "signUp" });
    },
    completedLogIn: function (data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autenticación Exitosa");
      this.verifyAuth();
    },
    completedSignUp: function (data) {
      alert("Registro Exitoso");
      this.completedLogIn(data);
    },
    loadHome: function () {
      this.$router.push({ name: "Home" });
    },
    logOut: function () {
      localStorage.clear();
      alert("Sesion Cerrada");
      this.verifyAuth();
    },
    loadRequestUser: function () {
      this.$router.push({ name: "RequestUser" });
    },
    loadDeleteUser: function () {
      this.$router.push({ name: "DeleteUser" });
    },
    loadPutUser: function () {
      this.$router.push({ name: "PutUser" });
    },
    completedRequestUser: function (data) {
      alert("Consulta exitosa");
      this.completedRequestUser(data);
    },
    loadPostpsalud: function () {
      this.$router.push({ name: "Postpsalud" });
    },
    loaddeletepsalud: function () {
      this.$router.push({ name: "deletepsalud" });
    },
    loadgetpsalud: function () {
      this.$router.push({ name: "getpsalud" });
    },
    loadputpsalud: function () {
      this.$router.push({ name: "putpsalud" });
    },
  },
  created: function () {
    this.verifyAuth();
  },
};
</script>
<style>
body {
  margin: 0 0 0 0;
}

.header {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;

  background-color: #00dcdc;
  color: #e5e7e9;
  font-size: 18px;

  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header h1 {
  width: 20%;
  text-align: center;
}

.header nav {
  height: 100%;
  width: 20%;

  display: flex;
  justify-content: space-around;
  align-items: center;

  font-size: 20px;
}

.header nav button {
  color: #e5e7e9;
  background: #1c588c;
  border: 1px solid #e5e7e9;

  border-radius: 5px;
  padding: 10px 20px;
}

.header nav button:hover {
  color: #1c588c;
  background: #e5e7e9;
  border: 1px solid #e5e7e9;
}

.main-component {
  height: 75vh;
  margin: 0%;
  padding: 0%;

  background: url("./assets/Medicine3.jpg");
}

.footer {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;

  background-color: #00dcdc;
  color: #e5e7e9;
}

.footer h2 {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: right;
  align-items: center;
}
</style>
