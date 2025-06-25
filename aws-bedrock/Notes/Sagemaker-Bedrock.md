
---

## ✅ Key Steps

### 1. Access Bedrock IDE
- Go to AWS Console → SageMaker → Unified Studio.
- Create a **Unified Studio Domain**.

### 2. Configure Authentication
- Use **IAM credentials** or configure **SSO (optional)**.

### 3. Open Bedrock IDE
- Inside Unified Studio, launch the **Bedrock IDE**.

### 4. Create a Project
- Choose **Generative AI application development**.
- Click **Create Project** and follow the wizard.

### 5. Build a Chat Agent App
- Click **Build Chat Agent**.
- Choose from available models (only those with access).
- Adjust settings like **guardrails** and **inference parameters**.

### 6. Monitor Usage
- Use **CloudWatch Logs** or **S3** for invocation logging.
- Create a log group and IAM role as needed.

---

## 📝 Notes

- You must **request access** to each model (e.g., Claude, Titan, Jurassic-2) before it appears in the IDE dropdown.
- Bedrock IDE is now fully integrated into **SageMaker Unified Studio**.
- Monitor and optimize model usage via **CloudWatch** or export logs to **S3**.

---

## 📎 References

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html)
- [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)

---

