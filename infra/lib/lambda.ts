import { Duration, Stack, StackProps } from 'aws-cdk-lib';
import { aws_lambda as lambda } from 'aws-cdk-lib'
import { aws_iam as iam } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as path from 'path';

export class LambdaStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const secretSantaLambda = new lambda.Function(this, 'secretSanta', {
      functionName: "secret-santa",
      timeout: Duration.minutes(1),
      environment: { "SES_EMAIL_FROM": String(process.env.SES_EMAIL_FROM) },
      runtime: lambda.Runtime.PYTHON_3_9,
      code: lambda.Code.fromAsset(path.join(__dirname, '../../lambda'), { exclude: ['venv/**', 'test/**', 'requirements.txt'] }),
      handler: 'src.secret_santa.lambda_handler'
    });

    const sesPolicy = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        'ses:SendEmail',
        'ses:SendRawEmail',
        'ses:SendTemplatedEmail',
      ],
      resources: [
        `arn:aws:ses:${process.env.AWS_REGION}:${Stack.of(this).account
        }:identity/${process.env.SES_EMAIL_FROM}`,
      ],
    })

    secretSantaLambda.addToRolePolicy(sesPolicy)
  }
}
