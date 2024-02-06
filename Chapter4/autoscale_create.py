import boto3

def autoscale_create():
    autoscaling = boto3.client('autoscaling')

    #create a launch configuration for use in autoscaling
    # autoscaling.create_launch_configuration(
    #     LaunchConfigurationName="book_configuration",
    #     ImageId="ami-051f7e7f6c2f40dc1",
    #     InstanceType="t2.micro",
    # )

    # #create an autoscaling group with your launch configuration
    # autoscaling.create_auto_scaling_group(
    # AutoScalingGroupName="book_autoscaler",
    #     LaunchConfigurationName="book_configuration",
    #     MinSize=2,
    #     MaxSize=5,
    #     DesiredCapacity=2,
    #     AvailabilityZones=['us-east-1a', 'us-east-1b'],
    # )

    # #create a policy for your autoscaling group
    # autoscaling.put_scaling_policy(
    #     AutoScalingGroupName="book_autoscaler",
    #     PolicyName="book_scale",
    #     PolicyType='TargetTrackingScaling',
    #     TargetTrackingConfiguration={
    #         'PredefinedMetricSpecification': {
    #             'PredefinedMetricType': 'ASGAverageCPUUtilization'
    #         },
    #         'TargetValue': 70
    #     }
    # )

    #update policy to 80 percent
    autoscaling.put_scaling_policy(
        AutoScalingGroupName="book_autoscaler",
        PolicyName="book_scale",
        PolicyType='TargetTrackingScaling',
        TargetTrackingConfiguration={
            'PredefinedMetricSpecification': {
                'PredefinedMetricType': 'ASGAverageCPUUtilization'
            },
            'TargetValue': 80
        }
    )

if __name__ == "__main__":
    autoscale_create()