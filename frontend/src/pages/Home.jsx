import { motion } from "framer-motion";
import {
  ArrowRight,
  Sparkles,
  Search,
  Brain,
  Shirt,
  BarChart3,
} from "lucide-react";
import { useNavigate } from "react-router-dom";

import "../styles/home.css";

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="home-page">

      {/* Animated background */}
      <div className="home-background">

        <div className="gradient-orb orb-one" />
        <div className="gradient-orb orb-two" />
        <div className="gradient-orb orb-three" />

        <div className="grid-overlay" />

        <div className="floating-line line-one" />
        <div className="floating-line line-two" />

      </div>

      {/* Dark overlay */}
      <div className="home-overlay" />

      {/* Floating fashion-tech cards */}

      <motion.div
        className="floating-card card-one"
        initial={{ opacity: 0, x: -40 }}
        animate={{
          opacity: 1,
          x: 0,
          y: [0, -10, 0],
        }}
        transition={{
          opacity: { duration: 1 },
          x: { duration: 1 },
          y: {
            duration: 5,
            repeat: Infinity,
            ease: "easeInOut",
          },
        }}
      >
        <div className="floating-icon">
          <Search size={18} />
        </div>

        <div>
          <span>SMART SEARCH</span>
          <strong>Find any style</strong>
        </div>
      </motion.div>

      <motion.div
        className="floating-card card-two"
        initial={{ opacity: 0, x: 40 }}
        animate={{
          opacity: 1,
          x: 0,
          y: [0, 12, 0],
        }}
        transition={{
          opacity: { duration: 1, delay: 0.3 },
          x: { duration: 1, delay: 0.3 },
          y: {
            duration: 6,
            repeat: Infinity,
            ease: "easeInOut",
          },
        }}
      >
        <div className="floating-icon">
          <Brain size={18} />
        </div>

        <div>
          <span>AI INTELLIGENCE</span>
          <strong>Ask your data</strong>
        </div>
      </motion.div>

      <motion.div
        className="floating-card card-three"
        initial={{ opacity: 0, y: 30 }}
        animate={{
          opacity: 1,
          y: [0, -8, 0],
        }}
        transition={{
          opacity: { duration: 1, delay: 0.6 },
          y: {
            duration: 5,
            repeat: Infinity,
            ease: "easeInOut",
          },
        }}
      >
        <div className="floating-icon">
          <Shirt size={18} />
        </div>

        <div>
          <span>PRODUCT INTELLIGENCE</span>
          <strong>1000+ styles</strong>
        </div>
      </motion.div>

      {/* Main content */}

      <motion.main
        className="home-content"
        initial="hidden"
        animate="visible"
      >

        {/* Badge */}

        <motion.div
          className="home-badge"
          variants={{
            hidden: {
              opacity: 0,
              y: 20,
            },
            visible: {
              opacity: 1,
              y: 0,
            },
          }}
          transition={{
            duration: 0.7,
          }}
        >
          <Sparkles size={15} />

          <span>
            AI-POWERED FASHION INTELLIGENCE
          </span>

          <span className="badge-dot" />
        </motion.div>

        {/* WFX title */}

        <motion.div
          className="brand-wrapper"
          variants={{
            hidden: {
              opacity: 0,
              scale: 0.92,
            },
            visible: {
              opacity: 1,
              scale: 1,
            },
          }}
          transition={{
            duration: 0.9,
            delay: 0.15,
            ease: "easeOut",
          }}
        >
          <div className="brand-glow" />

          <h1 className="home-title">
            WFX
          </h1>
        </motion.div>

        {/* Main heading */}

        <motion.h2
          className="home-heading"
          variants={{
            hidden: {
              opacity: 0,
              y: 25,
            },
            visible: {
              opacity: 1,
              y: 0,
            },
          }}
          transition={{
            duration: 0.8,
            delay: 0.3,
          }}
        >
          Fashion intelligence,
          <br />

          <span>
            reimagined.
          </span>
        </motion.h2>

        {/* Description */}

        <motion.p
          className="home-description"
          variants={{
            hidden: {
              opacity: 0,
              y: 20,
            },
            visible: {
              opacity: 1,
              y: 0,
            },
          }}
          transition={{
            duration: 0.8,
            delay: 0.45,
          }}
        >
          Explore products, analyze business data,
          discover similar garments and interact
          with your fashion ERP through AI.
        </motion.p>

        {/* CTA */}

        <motion.button
          className="home-button"
          variants={{
            hidden: {
              opacity: 0,
              y: 20,
            },
            visible: {
              opacity: 1,
              y: 0,
            },
          }}
          transition={{
            duration: 0.8,
            delay: 0.6,
          }}
          whileHover={{
            scale: 1.04,
          }}
          whileTap={{
            scale: 0.97,
          }}
          onClick={() => navigate("/dashboard")}
        >
          <span>Enter WFX</span>

          <span className="button-icon">
            <ArrowRight size={18} />
          </span>
        </motion.button>

        {/* Feature indicators */}

        <motion.div
          className="home-features"
          initial={{
            opacity: 0,
            y: 15,
          }}
          animate={{
            opacity: 1,
            y: 0,
          }}
          transition={{
            duration: 0.8,
            delay: 0.85,
          }}
        >

          <div className="feature-item">
            <BarChart3 size={16} />
            <span>Business Analytics</span>
          </div>

          <div className="feature-separator" />

          <div className="feature-item">
            <Search size={16} />
            <span>Smart Search</span>
          </div>

          <div className="feature-separator" />

          <div className="feature-item">
            <Brain size={16} />
            <span>AI Intelligence</span>
          </div>

        </motion.div>

      </motion.main>

      {/* Bottom scroll indicator */}

      <motion.div
        className="home-scroll"
        initial={{
          opacity: 0,
        }}
        animate={{
          opacity: 1,
        }}
        transition={{
          delay: 1.2,
          duration: 1,
        }}
      >
        <span>EXPLORE WFX</span>

        <motion.div
          className="scroll-line"
          animate={{
            scaleY: [0.4, 1, 0.4],
            opacity: [0.4, 1, 0.4],
          }}
          transition={{
            duration: 2,
            repeat: Infinity,
            ease: "easeInOut",
          }}
        />
      </motion.div>

    </div>
  );
}