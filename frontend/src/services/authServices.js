const authService = {
    async login(credentials) {
      // Simulate API call
      await new Promise((resolve) => setTimeout(resolve, 1000));
        console.log(credentials);
        console.log(credentials.email);
        console.log(credentials.password);
      if (credentials.email === "demo@example.com" && credentials.password === "password") {
        const userData = { id: 1, email: credentials.email, name: "Demo User" };
        return { success: true, user: userData, token: "test_token" };  // Added token for example
      }

      return { success: false, error: 'Invalid credentials' };
    },

    async register(credentials) {
      // Simulate API call
      await new Promise((resolve) => setTimeout(resolve, 1000));

      const userData = {
        id: Date.now(),
        email: credentials.email,
        name: credentials.name,
      };

      return { success: true, user: userData, token: "test_token" };  // Added token for example
    },
  };

  export default authService;