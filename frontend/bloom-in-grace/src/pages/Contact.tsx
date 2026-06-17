import Layout from "../components/Layout";

function Contact() {
  return (
    <Layout>
      <section className="max-w-4xl mx-auto px-6 py-20">

        <h1 className="text-5xl font-bold text-[#4A3F35]">
          Contact Us
        </h1>

        <p className="mt-6 text-lg text-[#7B6F63] leading-relaxed">
          We'd love to hear from you. Whether you have a question about a
          resource, need help accessing a download, or simply want to connect,
          feel free to reach out.
        </p>

        <div className="mt-12 bg-[#F8F3EE] rounded-2xl p-8">

          <h2 className="text-2xl font-semibold text-[#4A3F35]">
            Get In Touch
          </h2>

          <div className="mt-6 space-y-4">

            <div>
              <p className="font-semibold text-[#4A3F35]">
                Email
              </p>

              <p className="text-[#7B6F63]">
                miriamgatei2001@gmail.com
              </p>
            </div>

            <div>
              <p className="font-semibold text-[#4A3F35]">
                Response Time
              </p>

              <p className="text-[#7B6F63]">
                Within 1–2 business days
              </p>
            </div>

          </div>

        </div>

      </section>
    </Layout>
  );
}

export default Contact;