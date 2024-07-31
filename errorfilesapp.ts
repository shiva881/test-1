#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { GluestackStack } from '../lib/gluestack-stack';
import { AthenastackStack } from '../lib/athenastack-stack';
import { LambdastackStack } from '../lib/lambdastack-stack';
import { SagemakerstackStack } from '../lib/sagemakerstack-stack';

const app = new cdk.App();

const env = {
  account: process.env.CDK_DEFAULT_ACCOUNT || '111111111111',  // Dummy account ID
  region: process.env.CDK_DEFAULT_REGION || 'us-east-1',  // Dummy region
};

new GluestackStack(app, 'GlueStack', { env });
new AthenastackStack(app, 'AthenaStack', { env });
new LambdastackStack(app, 'LambdaStack', { env, athenaWorkGroup: 'primary' });
new SagemakerstackStack(app, 'SageMakerStack', { env });
