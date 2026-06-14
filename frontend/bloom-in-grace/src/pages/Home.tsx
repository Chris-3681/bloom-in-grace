import Layout from "../components/Layout";
import Hero from "../components/Hero";
import FeaturedProducts from "../components/FeaturedProducts";
import AboutSection from "../components/AboutSection";

function Home() {
  return (
    <Layout>
      <Hero />
      <FeaturedProducts />
      <AboutSection />
    </Layout>
  );
}

export default Home;