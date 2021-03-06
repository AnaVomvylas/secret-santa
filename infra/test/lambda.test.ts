import * as cdk from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import {LambdaStack} from '../lib/lambda';

test('Lambda Function Created', () => {
  const app = new cdk.App();
  const stack = new  LambdaStack(app, 'MyTestStack');
  const template = Template.fromStack(stack);

  template.hasResourceProperties('AWS::Lambda::Function', {
    FunctionName: "secret-santa"
  });
});
