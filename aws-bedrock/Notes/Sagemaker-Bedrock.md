
---

## 🧱 Key Concepts

- **Amazon Bedrock IDE** is embedded inside **SageMaker Unified Studio**.
- **Unified Studio Domain** must be created before launching the IDE.
- You can authenticate using either:
  - AWS **IAM credentials**, or
  - **SSO** via AWS Identity Center / SAML.

---

## 🧠 Project Setup Steps

1. **Create a Unified Studio Domain** in SageMaker.
2. **Configure networking** using Quick or Manual setup.
3. **(Optional)** Configure SSO access.
4. **Launch Unified Studio**, then go to **Bedrock IDE**.
5. **Create a new project** for "Generative AI Application Development."
6. **Create a Chat Agent App** and select a model from the dropdown:
   - Only models you've been granted access to will appear.
7. **Customize your app**:
   - Prompt with examples
   - Configure guardrails
   - Tune inference parameters (`temperature`, `top_p`)
8. **Save the app** using the pencil icon.

---

## 📊 Monitor & Log Model Usage

You can enable **invocation logging** to track requests, responses, and metadata:

1. Go to **Bedrock Console → Settings → Model Invocation Logging**.
2. Enable logging and choose:
   - **CloudWatch Logs** (recommended)
   - **S3 Bucket** (optional)
3. **Create IAM role** if prompted and assign it.
4. Your invocation data is now available for audit and monitoring.

---

## 📌 Summary

| Component             | Purpose                                          |
|----------------------|--------------------------------------------------|
| SageMaker Unified Studio | Development environment for Bedrock IDE     |
| Unified Studio Domain   | Required to access Bedrock IDE                |
| Bedrock IDE             | Model development, prompt design, app creation |
| CloudWatch Logs         | Monitor model usage and invocation metadata    |

---

> 💡 Tip: Always request model access in advance through the AWS Bedrock Console for your desired models (e.g., Claude, Titan, Cohere).

---

## ✅ Example Use Case

- Build a **Chat Agent App** using Titan Text Lite
- Use quick-start prompts to test generation
- Configure guardrails to filter outputs
- Save and deploy app
- Monitor behavior via CloudWatch

---

Let me know if you'd like a diagram version in PNG or editable file format (e.g., Draw.io)!
