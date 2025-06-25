# Building a Generative AI Chat Agent Application with Amazon SageMaker Unified Studio and Bedrock

This guide outlines the steps to create and deploy a Generative AI Chat Agent application using Amazon SageMaker Unified Studio (formerly Bedrock Studio) and Amazon Bedrock.

---

## Workflow

Follow these steps to set up your environment, create a project, and experiment with your chat agent app.

1.  **Go to SageMaker Console**
    * Navigate to the Amazon SageMaker service in your AWS Console.

2.  **Create Unified Studio Domain**
    * This is your central hub for SageMaker resources.
    * **Choose Setup Option:**
        * **Quick Setup:** For rapid deployment with default settings.
        * **Manual Setup:** For advanced configurations, such as specifying a custom VPC and subnets.

3.  **Configure SSO (Optional)**
    * Determine how users will authenticate to the Studio environment.
    * **Use IAM credentials:** For direct AWS Identity and Access Management (IAM) based authentication.
    * **Use SSO (Identity Center or SAML):** For integrated single sign-on using AWS IAM Identity Center (formerly AWS SSO) or a SAML-based identity provider.

4.  **Access Bedrock IDE (formerly Bedrock Studio)**
    * Once your Unified Studio Domain is set up, you will be able to access the Bedrock IDE environment within it.

5.  **Open Unified Studio (SageMaker)**
    * Launch the SageMaker Unified Studio interface.

6.  **Create a Project**
    * Within Unified Studio, initiate the creation of a new project.

7.  **Select "Generative AI Application Development"**
    * Choose this template for building AI applications leveraging Generative AI capabilities.

8.  **Create Chat Agent App**
    * Select the option to create a new chat agent application.

9.  **Select Model from Dropdown**
    * From the available options, choose the Foundation Model you wish to use for your chat agent.
    * *Note: Only models for which you have approved access will be displayed in the dropdown.*

10. **Experiment with your App**
    * Once your app is created, you can start experimenting with its behavior:
        * **Quick-start prompts:** Test predefined prompts to see the model's responses.
        * **Guardrails (content filters):** Implement and test content filters to ensure safe and appropriate outputs.
        * **Inference Parameters:** Adjust parameters like:
            * **Temperature:** Controls the randomness of the output (higher = more creative/less deterministic).
            * **Top P:** Controls the diversity of the output by sampling from a cumulative probability distribution.

11. **Save App**
    * Save your application configuration and any changes you've made.

12. **Monitor Usage**
    * Keep track of your application's performance and usage patterns.

13. **Enable Invocation Logging**
    * Activate logging for all invocations of your chat agent. This is crucial for monitoring, debugging, and auditing.

14. **Send Logs To:**
    * Configure where your invocation logs will be stored:
        * **CloudWatch Log Group:** Send logs to an Amazon CloudWatch Log Group (create a new one if needed).
        * **S3 Bucket (optional):** Optionally, send logs to an Amazon S3 bucket for long-term storage or further analysis.

15. **Done! ✅**

You have successfully set up and configured your Generative AI Chat Agent application.
