import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { PayPalScriptProvider } from "@paypal/react-paypal-js";
import { Toaster } from "react-hot-toast";

import App from "./App";
import "./index.css";

console.log(
  "PayPal Client ID:",
  import.meta.env.VITE_PAYPAL_CLIENT_ID
);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <BrowserRouter>
      <PayPalScriptProvider
        options={{
          clientId: import.meta.env.VITE_PAYPAL_CLIENT_ID,
          currency: "USD",
          intent: "capture",
        }}
      >
        <App />
        <Toaster position="top-center" />
      </PayPalScriptProvider>
    </BrowserRouter>
  </React.StrictMode>
);