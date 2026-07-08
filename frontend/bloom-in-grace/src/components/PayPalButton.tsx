import axios from "axios";
import { useNavigate } from "react-router-dom";
import { PayPalButtons } from "@paypal/react-paypal-js";
import API_URL from "../config/api";

type PayPalButtonProps = {
  slug: string;
  email: string;
};

function PayPalButton({
  slug,
  email,
}: PayPalButtonProps) {

  const navigate = useNavigate();

  return (
    <PayPalButtons
      style={{
        layout: "vertical",
        color: "gold",
        shape: "rect",
        label: "paypal",
      }}

      createOrder={async () => {

        if (!email.trim()) {
          alert("Please enter your email before continuing.");
          throw new Error("Missing email");
        }

        const response = await axios.post(
          `${API_URL}/create-paypal-order`,
          {
            slug,
          }
        );

        return response.data.id;
      }}

      onApprove={async (data) => {

        try {

          const response = await axios.post(
            `${API_URL}/capture-paypal-order`,
            {
              orderID: data.orderID,
              slug,
              email,
            }
          );

          const {
            success,
            download_token,
            error
          } = response.data;

          if (!success) {
            alert(error || "Payment failed.");
            return;
          }

          // Store token only for this browser session
          sessionStorage.setItem(
            "download_token",
            download_token
          );

          navigate("/success");

        } catch (err) {

          console.error(err);

          alert(
            "Something went wrong while confirming your payment."
          );
        }

      }}

      onCancel={() => {
        navigate("/cancel");
      }}

      onError={(err) => {
        console.error("PayPal Error:", err);
        alert("Something went wrong while processing your payment.");
      }}
    />
  );
}

export default PayPalButton;