package per.study.aws.service;

import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.regions.DefaultAwsRegionProviderChain;
import com.amazonaws.services.securitytoken.AWSSecurityTokenService;
import com.amazonaws.services.securitytoken.AWSSecurityTokenServiceClientBuilder;
import com.amazonaws.services.securitytoken.model.AssumeRoleRequest;
import com.amazonaws.services.securitytoken.model.AssumeRoleResult;
import org.springframework.stereotype.Service;

@Service
public class AmazonService {

    public AWSCredentials getCredentials() {
        AWSSecurityTokenService client = AWSSecurityTokenServiceClientBuilder.standard()
            .withRegion(determineClientRegion())
            .build();

        AssumeRoleRequest request = new AssumeRoleRequest()
            .withRoleArn("arn:aws:iam::767397978317:role/JenkinsRole")
            .withRoleSessionName("Jenkins")
            .withDurationSeconds(3600);

        AssumeRoleResult assumeRoleResult = client.assumeRole(request);

        return new BasicAWSCredentials(assumeRoleResult.getCredentials().getAccessKeyId(), assumeRoleResult.getCredentials().getSecretAccessKey());
    }

    private static String determineClientRegion() {
        DefaultAwsRegionProviderChain sdkRegionLookup = new DefaultAwsRegionProviderChain();

        return sdkRegionLookup.getRegion();
    }
}
