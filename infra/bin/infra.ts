#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaStack } from '../lib/lambda';

const env = { account: process.env.AWS_ACCOUNT, region: process.env.AWS_REGION }
const app = new cdk.App();

new LambdaStack(app, 'InfraStack', {
  env
});
