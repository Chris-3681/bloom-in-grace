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

        const response = await axios.post(
          `${API_URL}/capture-paypal-order`,
          {
            orderID: data.orderID,
            slug,
            email,
          }
        );

        if (response.data.success) {
          navigate("/success");
        } else {
          alert(response.data.error || "Payment failed.");
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